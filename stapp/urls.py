from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from video.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('video.urls')),
    url(r'^browser-version', direct_to_template, {'template': 'browser-version.html'}), 
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

