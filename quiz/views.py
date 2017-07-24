import json
from urllib.parse import urlparse, unquote

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from rest_framework.parsers import JSONParser

from .forms import LoginForm
from .models import Quiz, QuizSession


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'login.html'


def login_view(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        data = serializers.serialize('json', [user])
        return HttpResponse(data, status=200)
    return HttpResponse('Invalid username/password!', status=404)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class SignupView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'


class QuizListView(generic.ListView):
    template_name = 'quizlist.html'
    context_object_name = 'quizzes'
    queryset = Quiz.published.all()


def quiz_form(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quiz_form.html', {'quiz': quiz})


def quiz_results(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    return render(request, 'quiz_results.html', {'session': session})


def check(request, quiz_id):
    quizdata = request.COOKIES.get('quizdata')
    quizdata = json.loads(json.loads(unquote(quizdata)))
    quiz = get_object_or_404(Quiz, id=int(quiz_id))
    session = QuizSession(quiz=quiz, user=request.user, date_taken=timezone.now().date())
    correct = 0
    wrong = 0
    answers = {}
    for question in quiz.question_set.all():
        answerid = quizdata[str(question.id)]
        answers[question.id] = answerid
        correct_choices = question.choice_set.filter(is_correct=True).values_list('id')[0]
        if answerid in correct_choices:
            correct += 1
        else:
            wrong += 1
    session.answers = answers
    session.score = correct
    session.save()
    return HttpResponse(session.id, status=200)