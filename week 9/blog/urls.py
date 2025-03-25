
from django.urls import path, include
from .views import PostsListCreateAPIView

urlpatterns = [
        # notice how we need to call .as_view() because this view is class based. if it was a function-based view we won't need to call .as_view()
        path('posts/', PostsListCreateAPIView.as_view(), name='post-list-create'),
]
