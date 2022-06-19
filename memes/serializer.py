import os

from django.conf import settings
from rest_framework import serializers

from memes.models import Post


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'photo_id',
            'owner_id',
            'likes',
            'priority',
            'updated',
            'image'
        )

    def get_image(self, obj):
        return f'{settings.MEDIA_URL}memes/{obj.photo_id}.jpg'
