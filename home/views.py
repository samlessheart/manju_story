from email import message
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .forms import photoForm, storyForm, videoForm, commentForm
from .models import MyPhoto, MyVideo,  Story, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def home(request):
    photos = MyPhoto.objects.all()[:3]
    context = {"photos_obj":photos}
    return render(request, "home/home.html", context)


def profile(request):
    return render(request, "home/profile.html")

def photolist(request):
    photos = MyPhoto.objects.all()
    context = {"photos":photos}
    return render(request, "home/photolist.html", context)

def photodet(request, pk):
    photo_obj = MyPhoto.objects.get(id = pk)
    comments = Comment.objects.filter(photo = photo_obj)
    form = commentForm()
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            main = form.cleaned_data["main"]
            name = form.cleaned_data["name"]
            comment_obj = Comment.objects.create(main=main, name=name, photo=photo_obj)
            comment_obj.save()
            messages.success(request, f"Thanks for your valuable Comment!")
            return redirect("photodet", photo_obj.id)
    context = {"photo": photo_obj,  "form":form, "comments":comments}
    
    return render(request, "home/photodet.html", context)

def storylist(request):
    stories = Story.objects.all()
    context = {"stories": stories}
    return render(request, "home/storylist.html", context)

def videolist(request):
    videos = MyVideo.objects.all()
    context = {"videos":videos}
    return render(request, "home/videolist.html", context)

@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def addphoto(request):
    form  = photoForm()
    context = {'form':form}
    if request.method == 'POST':
        form = photoForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print("form is valid")
            image_link = form.cleaned_data.get('image_link')
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            myphoto = MyPhoto.objects.create(image_link=image_link, title=title, description=description)
            myphoto.save()
            messages.success(request, f"{myphoto} Manjunath you added the new photo, it looks nice..!")
            return redirect('home')
        else:
            print("form is not valid")            
            messages.warning(request, f" Manjunath you seem to have made a mistake, apparently..!")

    return render(request, "home/addphoto.html", context)


@login_required
def addstory(request):
    form  = storyForm()
    context = {'form':form}
    if request.method == 'POST':
        form = storyForm(request.POST)
        if form.is_valid():    
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            mystory = Story.objects.create( title=title, post=post)
            mystory.save()
            messages.success(request, f"{mystory} Manjunath you added the new Story, it looks nice..!")
            return redirect('home')
        else:
            messages.warning(request, f" Manjunath you may have made a mistake, apparently..!")                     
    return render(request, "home/addstory.html", context)


@login_required
def addvideo(request):
    form  = videoForm()
    context = {'form':form}
    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("form is valid")
            video_link = form.cleaned_data.get('video_link')
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            myvideo = MyVideo.objects.create(video_link=video_link, title=title, description=description)
            myvideo.save()
            messages.success(request, f"{myvideo} Manjunath you added the new photo, it looks nice..!")
            return redirect('home')
        else:
            print("form is not valid")            
            messages.warning(request, f" Manjunath you seem to have made a mistake, apparently..!")
    return render(request, "home/addvideo.html", context)



