from msilib.schema import Class
from django.db import models

# Create your models here.


class MyPhoto(models.Model):
    image_link = models.ImageField(upload_to='myphoto/', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
class MyVideo(models.Model):
    video_link = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title    


class Story(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    main = models.TextField()
    name = models.CharField(max_length=100)
    story = models.ForeignKey(Story, null=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(MyPhoto, null=True, on_delete=models.CASCADE)




    

    


    

    
