from django.db import models


class Post(models.Model):
    photo_id = models.IntegerField()
    owner_id = models.CharField(max_length=64)
    likes = models.IntegerField()
    priority = models.BooleanField(default=False)
