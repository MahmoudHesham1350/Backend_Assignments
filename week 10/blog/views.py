from django.shortcuts import render
from rest_framework import generics, viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import PostPageNumberPagination

# Create your views here.

# Creating an endpoint for listing all posts & creating a new post

class PostsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPageNumberPagination
    
    # When a request is sent, we need to set the author field to the user's username
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostsRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



class LikesAPIView(APIView):
    """
    LikesAPIView handles the like and unlike functionality for posts, as well as retrieving the list of likes for a specific post.

    Methods:
        post(request):
            Handles the creation or deletion of a like for a specific post.
            - If the post ID is not provided, returns a 400 Bad Request response.
            - If the post does not exist, returns a 404 Not Found response.
            - If the like already exists, it deletes the like and returns a 200 OK response with "unliked" status.
            - If the like does not exist, it creates a new like and returns a 201 Created response with "liked" status.

        get(request):
            Retrieves the list of likes for a specific post.
            - If the post ID is not provided, returns a 400 Bad Request response.
            - Returns a 200 OK response with the serialized list of likes and the total count of likes for the post.

    Attributes:
        permission_classes (list): Specifies that the API view requires the user to be authenticated.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post')
        if not post_id:
            return Response(
                {"status": "error", "message": "Post ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {"status": "error", "message": "Post not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        user = request.user
        like, created = Like.objects.get_or_create(post=post, user=user)

        if not created:
            like.delete()
            return Response({"status": "unliked"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "liked"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        post_id = self.request.query_params.get('post')
        if not post_id:
            return Response(
                {"status": "error", "message": "Post ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        likes = Like.objects.filter(post=post_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(
            {"likes": serializer.data, "likes_count": likes.count()},
            status=status.HTTP_200_OK
        )
        


class commentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



