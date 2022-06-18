from django.urls import path

from .api import RegisterAPI, SignInAPI, LogoutAPI

app_name = 'memes'

urlpatterns = [
    path('register', RegisterAPI.as_view()),
    path('auth', SignInAPI.as_view()),
    path('logout', LogoutAPI.as_view())
]
