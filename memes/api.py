import random

from django.conf import settings
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response

from .models import Post
from .serializer import PostSerializer


class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        priority_post = Post.objects.filter(priority=True).first()
        if priority_post is None:
            return Response(data=Post.objects.order_by('id').values(), status=status.HTTP_200_OK)
        post = Post.objects.get(priority=True)
        post_likes = post.likes

        first_part = Post.objects.filter(likes__lt=post_likes).order_by('likes')
        last_part = Post.objects.all().exclude(likes__lt=post_likes).order_by('?')

        return Response(data=[model_to_dict(post)] + list(first_part.values()) + list(last_part.values()), status=status.HTTP_200_OK)


class LikeAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if request.query_params.get('photo_id') is None:
            return Response(data={
                'error': 'You forgot: photo_id parameter. Your request should look like: HOST/post/like?photo_id=457240792'
            }, status=status.HTTP_400_BAD_REQUEST)
        content = settings.CONNECTION.method('photos.get', {'owner_id': settings.OWNER_ID, 'album_id': 283939598, 'extended': 1})
        photo = [x for x in content['items'] if x['id'] == int(request.query_params['photo_id'])]
        if photo:
            photo = photo[0]
        else:
            return Response(data={
                'error': 'Photo is not exists',
                'photos': [x['id'] for x in content['items']]
            }, status=status.HTTP_400_BAD_REQUEST)

        post = Post.objects.get(photo_id=photo['id'])
        try:
            if photo['likes']['user_likes']:
                settings.CONNECTION.method('likes.delete', {'type': 'photo', 'owner_id': settings.OWNER_ID, 'item_id': photo['id']})
                post.likes -= 1
                post.save()
                message = 'Unliked'
            else:
                settings.CONNECTION.method('likes.add', {'type': 'photo', 'owner_id': settings.OWNER_ID, 'item_id': photo['id']})
                post.likes += 1
                post.save()
                message = 'Liked'
        except Exception as e:
            return Response(data={'error': 'VK API down'})
        return Response(data={'message': message}, status=status.HTTP_200_OK)


class PriorityAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        photo_id = request.query_params.get('photo_id')
        if photo_id is None:
            return Response(data={
                'error': 'You forgot: photo_id parameter. Your request should look like: HOST/post/priority?photo=457240792'
            }, status=status.HTTP_400_BAD_REQUEST)

        priority = Post.objects.filter(priority=True).first()
        if priority:
            priority.priority = False
            priority.save()

        post = get_object_or_404(Post, photo_id=photo_id)
        post.priority = True
        post.save()

        return Response(data={'message': f'Post with id: {photo_id} now is priority'})

