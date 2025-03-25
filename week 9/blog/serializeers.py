from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # When dealing with foreign fields we have to define them this way first in our serializer class 
    # before adding them in the fields list.
    author = serializers.ReadOnlyField(source='author.username')
    # We used ReadOnlyField so that the client can't modify the author property of any posts.
    # i.e the author.username is only included in serialization and NOT deserialization

    class Meta:
        # The model that we need to serizlize
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        # The fields that will be serialized/deserialized

