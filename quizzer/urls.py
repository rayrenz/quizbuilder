from django.conf.urls import url

from .views import logout_view
from . import views


urlpatterns = [
    url(r'^quiz/(?P<pk>[0-9]+)/$', views.QuizView.as_view(), name='quiz_view'),
    url(r'^$', views.home, name='home'),
    url(r'^quizzes/$', views.QuizListView.as_view(), name='quizzes'),
    url(r'^check/(?P<quiz_id>[0-9]+)/$', views.check, name='check'),
    url(r'^quiz/(?P<pk>[0-9]+)/results/$', views.SessionResultsView.as_view(), name='session_results'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
