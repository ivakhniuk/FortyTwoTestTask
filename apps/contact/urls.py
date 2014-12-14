from django.conf.urls import patterns, include, url

from contact import views


urlpatterns = patterns('',
    url(r'^edit/$', views.edit, name='edit'),
)
