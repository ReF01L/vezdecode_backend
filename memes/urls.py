from django.urls import path

from .api import PostListAPI, LikeAPI, PriorityAPI, DashboardAPI, PostRetrieveAPI

app_name = 'memes'

urlpatterns = [
    path('posts', PostListAPI.as_view()),
    path('posts/<int:pk>', PostRetrieveAPI.as_view()),
    path('post/like', LikeAPI.as_view()),
    path('post/priority', PriorityAPI.as_view()),
    path('dashboard', DashboardAPI.as_view())
]
