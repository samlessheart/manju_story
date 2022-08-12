import fileinput
from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField, ImageField, 
                            FileInput, ClearableFileInput)
from .models import Story, MyPhoto, Comment, MyVideo


class storyForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'post']


        widgets = {
                'title' : Textarea(attrs={'rows': 1,'class': 'form-control col-6'}),
                'post': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-6'}),
                
            }

class photoForm(forms.ModelForm):
    class Meta:
        model = MyPhoto
        fields = ['title', 'image_link', 'description']
        labels = {'image_link': "Upload Image"}

        widgets = {
                'title' : Textarea(attrs={'rows': 1,'class': 'form-control col-6'}),
                'image_link': ClearableFileInput(),
                'description' : Textarea(attrs={ 'rows': 1, 'class': 'form-control col-6'}),

            }

class videoForm(forms.ModelForm):
    class Meta:
        model = MyVideo
        fields = ['title', 'video_link', 'description']
        labels = {'video_link': "Upload Video"}

        widgets = {
                'title' : Textarea(attrs={'rows': 1,'class': 'form-control col-6'}),
                'video_link': ClearableFileInput(),
                'description' : Textarea(attrs={ 'rows': 1, 'class': 'form-control col-6'}),

            }


class commentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['main', 'name']
        labels = {'main': "Comment", 'name': "Your Name"}

        widgets = {
                'main' : Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
                'name': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
                
            }