from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^quizzes/$', views.quiz_list, name='quiz_list'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', views.quiz_view, name='quiz_view'),
    url(r'^$', views.home, name='home'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/(?P<session_id>[0-9]+)/results/$', views.session_results, name='session_results'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
]
