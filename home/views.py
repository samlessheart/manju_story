from email import message
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .forms import photoForm, storyForm
from .models import MyPhoto,  Story
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    photos = MyPhoto.objects.all()[:10]
    context = {"photos_obj":photos}

    return render(request, "home/home.html", context)


def profile(request):
    return render(request, "home/profile.html")

def photolist(request):
    return render(request, "home/photolist.html")

def storylist(request):
    return render(request, "home/storylist.html")

def videolist(request):
    return render(request, "home/videolist.html")




@login_required
def addphoto(request):
    form  = photoForm()
    context = {'form':form}
    if request.method == 'POST':
        form = photoForm(request.POST)
        if form.is_valid():
            image_link = form.cleaned_data['image_link']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            myphoto = MyPhoto.objects.create(image_link=image_link, title=title, description=description)
            myphoto.save()

            messages.success(request, f"{myphoto} Manjunath you added the new photo, it looks nice..!")
            return redirect('home')
        else:
            messages.warning(request, f"{myphoto} Manjunath you seem to have made a mistake, apparently..!")
            

          
    return render(request, "home/addphoto.html", context)


@login_required
def addstory(request):
    form  = storyForm()
    context = {'form':form}
    if request.method == 'POST':
        form = storyForm(request.POST)
        if form.is_valid():
            
            title = form.cleaned_data['title']
            post = form.cleaned_data['description']

            mystory = MyPhoto.objects.create( title=title, post=post)
            mystory.save()

            messages.success(request, f"{mystory} Manjunath you added the new Story, it looks nice..!")
            return redirect('home')
        else:
            messages.warning(request, f" Manjunath you may have made a mistake, apparently..!")
            

          
    return render(request, "home/addstory.html", context)





