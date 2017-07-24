from django import template
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from ..models import QuizSession

register = template.Library()


@register.inclusion_tag('recent_quizzes.html')
def recent_quizzes(user_id):
    user = get_object_or_404(User, id=user_id)
    return {'sessions': QuizSession.objects.filter(user=user).order_by('-date_taken')}


@register.assignment_tag
def is_answered(session_id, choice_id):
    session = QuizSession.objects.get(id=session_id)
    for question in session.quiz.question_set.all():
        if choice_id == session.answers[question.id]:
            return True
    return False
