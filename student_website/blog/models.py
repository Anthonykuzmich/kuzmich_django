from django.db import models
from django.urls import reverse
from datetime import datetime, date

from django.contrib.auth.models import User


class Sphere(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog')


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    age = models.IntegerField(default=None)
    speciality = models.CharField(max_length=20)
    sphere = models.CharField(max_length=30, default=None)
    resume = models.TextField(default=None)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('blog')
