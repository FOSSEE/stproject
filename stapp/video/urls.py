from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('video.views',
    url(r'^login/$','user_login'),
    url(r'^register/$','user_register'),
    url(r'^view/$', 'show'),
    url(r'^view/(?P<video_id>\d+)/$', 'show'),
    url(r'^logout/$','user_logout'),

)

