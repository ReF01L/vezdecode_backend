from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response

from user.models import User
from .models import Post
from .serializer import PostSerializer


class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        priority_post = Post.objects.filter(priority=True).first()
        if priority_post is None:
            result = Post.objects.order_by('id').values()
            return Response(data={
                'photos': result,
                'count': len(result)
            }, status=status.HTTP_200_OK)
        post = Post.objects.get(priority=True)
        post_likes = post.likes

        first_part = Post.objects.filter(likes__lt=post_likes).order_by('-likes')
        last_part = Post.objects.all().exclude(likes__lt=post_likes).order_by('?')

        result = [model_to_dict(post)] + list(first_part.values()) + list(last_part.values())

        return Response(data={
            'photos': result,
            'count': len(result)
        }, status=status.HTTP_200_OK)


class LikeAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if request.session.get('user'):
            photo_id = request.query_params.get('photo_id')
            if photo_id is None:
                return Response(data={
                    'error': 'You forgot: photo_id parameter. Your request should look like: HOST/post/like?photo_id=457240792'
                }, status=status.HTTP_400_BAD_REQUEST)

            post = Post.objects.get(photo_id=photo_id)
            user = User.objects.get(pk=request.session.get('user')['id'])

            if user.post_liked.filter(user__post_liked=post).exists():
                post.likes -= 1
                user.post_liked.remove(post)
                message = 'Unliked'
            else:
                post.likes += 1
                user.post_liked.add(post)
                message = 'Liked'
            post.save()

            return Response(data={'message': message}, status=status.HTTP_200_OK)
        return Response('You should to sigh in first/ (Go to POST/ 127.0.0.1/login)', status=status.HTTP_400_BAD_REQUEST)


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


class DashboardAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
       posts = Post.objects.all()
        return Response(data={
            'best': posts.order_by('-likes').values('id', 'photo_id', 'likes', 'updated')[:5],
            'last_interaction': posts.order_by('-updated').values('id', 'photo_id', 'likes', 'updated')[:5],
            'count': len(posts.values())
        }, status=status.HTTP_200_OK)
