from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField)
from .models import Story, MyPhoto, Comment


class storyForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'post']


        widgets = {
                'title' : Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
                'post': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
                
            }

class photoForm(forms.ModelForm):
    class Meta:
        model = MyPhoto
        fields = ['title', 'image_link', 'description']

        widgets = {
                'title' : Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
                'image_link': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
                'description' : Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),

            }

class commentForm(forms.ModelForm):
    class Meta: 
        model = Comment()
        fields = ['main', 'name']


        widgets = {
                'main' : Textarea(attrs={'rows': 1,'class': 'form-control col-8'}),
                'name': Textarea(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
                
            }