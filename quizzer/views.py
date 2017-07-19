from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework import generics
from rest_framework.views import APIView

from .models import Quiz, QuizSession
from .forms import LoginForm
from .serializers import QuizSerializer, UserSerializer


class QuizListView(generics.ListAPIView):
    queryset = Quiz.published.all()
    serializer_class = QuizSerializer


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Quiz.objects.filter(id=quiz_id)[:1]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def quiz_list(request):
    if request.user.is_authenticated():
        quizzes = Quiz.published.exclude(expiration__lte=timezone.now())

        paginator = Paginator(quizzes, 20)  # 20 quizzes per page
        page = request.GET.get('page')

        try:
            quizzes = paginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            quizzes = paginator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page of results
            quizzes = paginator.page(paginator.num_pages)

        return render(request, 'quizzer/quiz_list.html', {'page': page, 'quizzes': quizzes})

    return redirect('quizzer:home')


def home(request):
    return render(request, 'index.html')


def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('quizzer:home'))
            message = 'Invalid username/password!'
    else:
        form = LoginForm()
    return render(request, 'quizzer/login.html', {'form': form, 'message': message})


def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        session = QuizSession(quiz=quiz, user=request.user, date_taken=timezone.now())
        correct = 0
        wrong = 0
        answers = {}
        for question in quiz.question_set.all():
            answer = question.choice_set.get(id=request.POST[str(question.id)])
            answers[question.id] = answer.id
            if answer in question.choice_set.filter(is_correct=True):
                correct += 1
            else:
                wrong += 1
        session.answers = answers
        session.score = correct
        session.save()
        return HttpResponseRedirect(reverse('quizzer:session_results', kwargs={'quiz_id': quiz.id,'session_id': session.id}))
    return render(request, 'quizzer/quizform.html', {'quiz': quiz, 'start': timezone.now()})


def session_results(request, quiz_id, session_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    session = get_object_or_404(QuizSession, quiz=quiz, id=session_id)

    results = dict()
    for question in quiz.question_set.all():
        results[question.id] = question.text

    return render(request, 'quizzer/quiz_results.html', {'results': results, 'session': session})


def logout_view(request):
    logout(request)
    return redirect('quizzer:home')


def register(request):
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quizzer:login'))
            # else:
            #     message = 'Passwords do not match'
    else:
        form = UserCreationForm()
    return render(request, 'quizzer/registration.html', {'message': message, 'form': form})
