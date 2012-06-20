from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from video.models import Video

def show(request):
    videos = Video.objects.all()
    if len(videos) == 0 :
        return HttpResponse("No videos in Database...")
    play_video = Video.objects.latest('created')
    vids = { 'videos' : videos , 'play' : play_video}
    return render_to_response('video/list_videos.html', vids)
    
