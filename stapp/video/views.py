from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from video.models import Video, Module

def show(request):
    videos = Video.objects.all()
    if len(videos) == 0 :
        return HttpResponse("No videos in Database...")

    #Get the latest video to display on the front page
    latest_video = Video.objects.latest('created')
    
    #Get last three modified modules
    latest_modules = Module.objects.order_by('-modified')


    context = { 'modules' : latest_modules , 'play' : latest_video}
    return render(request, 'video/home.html', context)
    
