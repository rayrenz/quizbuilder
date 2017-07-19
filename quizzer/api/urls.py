from django.conf.urls import url

from .. import views


urlpatterns = [
    url(r'^quizzes/$', views.QuizListView.as_view(), name='quizzes'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', views.QuizView().as_view(), name='quiz'),
    url(r'^users/$', views.UserListView.as_view(), name='users'),
]