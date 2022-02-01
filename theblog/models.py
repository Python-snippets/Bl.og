from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
    #   return reverse("article-detail", args=(str(self.id)) )
    # sends you to the home page 
        return reverse("home")  

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # if we delete the user all of its attribute will gets deleted automatically 
    bio = models.TextField(null=True)
    profile_pic =  models.ImageField(null=True, blank=True, upload_to="images/profile/")
    ##--------------------------------Social Links------------------------------##
    github = models.CharField(max_length=225, null=True, blank=True)
    website = models.CharField(max_length=225, null=True, blank=True)
    twitter = models.CharField(max_length=225, null=True, blank=True)
    instagram = models.CharField(max_length=225, null=True, blank=True)
    #null= models.CharField(max_length=225, null=True, blank=True) 

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=225)
    title_tag = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField(null=True)
    body = RichTextField(null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=225, default='Alpha')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") 

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
    #   return reverse("article-detail", args=(str(self.id)) )
    # sends you to the home page 
        return reverse("home")
    
