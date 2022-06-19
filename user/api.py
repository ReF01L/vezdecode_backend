from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, get_object_or_404, ListAPIView
from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer


class RegisterAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignInAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        if request.session.get('user') is None:
            user = get_object_or_404(User, login=request.data['login'])
            if user.password == request.data['password']:
                request.session['user'] = model_to_dict(user)
                return Response(data={'message': 'Accepted'}, status=status.HTTP_200_OK)
        return Response(data={'message': 'Canceled'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if request.session.get('user') is not None:
            del request.session['user']
            return Response(data={'message': 'Logout'}, status=status.HTTP_200_OK)
        return Response(data={'message': 'You are already logout'}, status=status.HTTP_200_OK)
