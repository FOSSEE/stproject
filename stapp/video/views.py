from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
import os
from video.forms import *
from video.models import *
from django.contrib.auth import login, logout, authenticate

def user_login(request):
    """Take the credentials of the user and log the user in."""

    user = request.user
    if user.is_authenticated():
        return redirect("/video/view/")

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            login(request, user)
            return redirect('/video/view/')
        else:
            form = UserLoginForm()
            context = {"form": form}
            return render_to_response('video/login.html', context,
                        context_instance=RequestContext(request))
    else:
        form = UserLoginForm()
        context = {"form": form}
        return render_to_response('video/login.html', context,
                                     context_instance=RequestContext(request))


def user_register(request):
    """ Register a new user.
    Create a user and corresponding profile and store roll_number also."""

    user = request.user
    if user.is_authenticated():
        return redirect("/video/view/")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u_name, pwd = form.save()

            new_user = authenticate(username = u_name, password = pwd)
            login(request, new_user)
            return redirect("/video/view/")
        
        else:
            return render_to_response('video/register.html',
                {'form':form},
                context_instance=RequestContext(request))
    else:
        form = UserRegisterForm()
        return render_to_response('video/register.html',
                {'form':form},
                context_instance=RequestContext(request))

def user_logout(request):
    user = request.user
    logout(request)
    return redirect('/video/login/')

def show(request,video_id=None):
    user = request.user
    if not user.is_authenticated():
        return redirect('/video/login/')
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
    
