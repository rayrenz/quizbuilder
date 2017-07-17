from django.conf.urls import url

from .views import quiz_view, home, session_results, logout_view, login_view, register


urlpatterns = [
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', quiz_view, name='quiz_view'),
    url(r'^$', home, name='home'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/(?P<session_id>[0-9]+)/results/$', session_results, name='session_results'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register, name='register'),
]
