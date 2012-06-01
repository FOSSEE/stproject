
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from video.views import *

admin.autodiscover()
from settings import URL_ROOT

if URL_ROOT.startswith('/'):
    URL_BASE = r'^%s/video/'%URL_ROOT[1:]
    ADMIN_BASE = r'^%s/admin/'%URL_ROOT[1:]
else:
    URL_BASE = r'^video/'
    ADMIN_BASE = r'^admin/'


urlpatterns = patterns('',
    url(URL_BASE, include('video.urls')),
    url(ADMIN_BASE, include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

