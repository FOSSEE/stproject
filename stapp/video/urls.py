from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('video.views',
    url(r'^$', 'show'),
    url(r'^view/(?P<video_id>\d+)/$', 'show'),
)

