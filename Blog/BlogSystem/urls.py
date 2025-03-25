from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    # URL to list all posts
    path('', views.listPosts, name='listPosts'),

    # URL to view a single post and its comments
    path('<int:pk>', views.listPost, name='listPost'),

    # URL to update a comment (edit)
    path('comment/<int:pk>/edit/', views.commentUpdate, name='commentUpdate'),

    # URL to delete a comment
    path('comment/<int:pk>/delete/', views.commentDelete, name='commentDelete'),

    # URL to create a new post
    path('create/', views.createPost, name='createPost'),

    # URL to update (edit) an existing post
    path('update/<int:pk>', views.updatePost, name='updatePost'),

    # URL to delete a post
    path('delete/<int:pk>', views.deletePost, name='deletePost'),
]
