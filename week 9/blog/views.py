from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializeers import PostSerializer

# Create your views here.

# Creating an endpoint for listing all posts & creating a new post

class PostsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # When a request is sent, we need to set the author field into the user's username
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


