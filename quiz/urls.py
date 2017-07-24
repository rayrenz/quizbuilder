from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^loginpage/$', views.LoginView.as_view(), name='login_get'),
    url(r'^loginpostdata/(?P<username>\w+)/(?P<password>\w+)/$', views.login_view, name='login_post'),
    url(r'^signuppage/$', views.SignupView.as_view(), name='signup'),
    url(r'^loggingout/$', views.logout_view, name='logout'),
    url(r'^quizzes/$', views.QuizListView.as_view(), name='quiz_list'),
    url(r'^startquiz/(?P<quiz_id>[0-9]+)/$', views.quiz_form, name='quiz_form'),
    url(r'^check/(?P<quiz_id>[0-9]+)/$', views.check, name='check'),
    url(r'^quizresults/(?P<session_id>[0-9]+)/$', views.quiz_results, name='quiz_results'),
]
