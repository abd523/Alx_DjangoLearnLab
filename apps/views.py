from django.shortcuts import render

# Create your views here.
from rest_framework import genrics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_serializer_class = UserRegisterSerializer