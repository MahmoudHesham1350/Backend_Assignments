from rest_framework import serializers
from .models import Post, Like, Comment

class PostSerializer(serializers.ModelSerializer):
    # When dealing with foreign fields properties we have to define them this way first in our serializer class 
    # before adding them in the fields list.
    author = serializers.ReadOnlyField(source='author.username')
    # We used ReadOnlyField so that the client can't modify the author property of any posts.
    # i.e the author.username is only included in serialization and NOT deserialization

    class Meta:
        # The model that we need to serizlize
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_date']
        # The fields that will be serialized/deserialized

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like

        fields = ['id', 'post', 'user']
        read_only_fields = ['user']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'comment', 'created_date']
        read_only_fields = ['user']

    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Post does not exist.")
        return value

