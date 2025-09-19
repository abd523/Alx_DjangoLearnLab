from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]    


# BookViewSet: Handles CRUD for Books with Token Authentication.
# Requires IsAuthenticated permission: Users must provide a valid token in headers.
# Tokens obtained via POST to /api/api-token-auth/ with username/password.
class BookViewSet(ModelViewSet):
    ...    