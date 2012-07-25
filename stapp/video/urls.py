from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('video.views',
    url(r'^$', 'show'),
    url(r'^view/(?P<video_id>\d+)/$', 'show'),
    url(r'^tags/$','show_tags_video'),
    url(r'^tags/(?P<tag_name>[a-zA-Z0-9_.]+)/$', 'show_tags_video'),
)

