from django.db import models

from memes.models import Post


class User(models.Model):
    login = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=24)
    post_liked = models.ManyToManyField(Post, null=True, blank=True)
