from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from video.models import *


def show(request,video_id=None):
    videos = Video.objects.all()
    if len(videos) == 0 :
        return HttpResponse("No videos in Database...")
    play_video = None
    if video_id != None :
        play_video = Video.objects.get(id = video_id)
    else:
        play_video = videos[len(videos)-1]
    vids = { 'videos' : videos , 'play' : play_video}
    return render_to_response('video/list_videos.html', vids)
    
