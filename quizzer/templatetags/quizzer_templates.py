from django import template

register = template.Library()

from ..models import QuizSession


@register.inclusion_tag('quizzer/recent_quizzes.html')
def recent_quizzes(user_id):
    latest_quizzes = QuizSession.objects.filter(user__id=user_id).order_by('-date_taken')[:5]
    return {'latest_quizzes': latest_quizzes}


@register.assignment_tag
def is_answered(session_id, choice_id):
    session = QuizSession.objects.get(id=session_id)
    for question in session.quiz.question_set.all():
        if choice_id == session.answers[question.id]:
            return True
    return False
