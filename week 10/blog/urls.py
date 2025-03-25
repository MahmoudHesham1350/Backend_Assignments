
from django.urls import path, include
from .views import PostsListCreateAPIView, PostsRetriveUpdateDestroyAPIView, commentViewSet
from .views import LikesAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comments', commentViewSet, basename='comments')

urlpatterns = [
        # notice how we need to call .as_view() because this view is class based. if it was a function-based view we won't need to call .as_view()
        path('posts/', PostsListCreateAPIView.as_view(), name='post-list-create'),
        path('posts/<int:pk>/', PostsRetriveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
        path('likes/', LikesAPIView.as_view(), name='likes'),
        path('', include(router.urls))
]
