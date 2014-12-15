from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from contact import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.person_view, name='person'),
    url(r'^logger/', include('logger.urls', namespace='logger')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
