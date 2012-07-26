from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from video.models import Video, Module
from taggit.models import Tag

def show(request):
    videos = Video.objects.all()
    if len(videos) == 0 :
        return HttpResponse("No videos in Database...")

    #Get the latest video to display on the front page
    latest_video = Video.objects.latest('created')
    return HttpResponse(latest_video.mykey)
    #Get last three modified modules
    latest_modules = Module.objects.order_by('-modified')[0:3]
    all_modules = Module.objects.order_by('modified')
    tags = Tag.objects.all()

    context = { 'latest_modules' : latest_modules , 'play' : latest_video, 'all_modules':all_modules,'tags':tags}
    return render(request, 'video/home.html', context)
    

def show_tags_video(request,tag_name=None):
    if tag_name==None:
        return redirect('/')
    videos = Video.objects.filter(tags__name__in=[tag_name])
    context = {'videos':videos}
    return render(request,'video/tag_video.html',context)

