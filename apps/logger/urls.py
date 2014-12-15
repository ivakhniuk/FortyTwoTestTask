from django.conf.urls import patterns, include, url

from logger import views


urlpatterns = patterns('',
    url(r'^$', views.logger_view, name='log'),
    url(r'^login/$', views.login_view, name='login')
)
