from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    # Show author's username instead of ID
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at']
        
        
        #why readonly we dont wnat user to send author 5 instead we assign from logged in users
        
class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at']
        
# When creating post:
# Client sends title + content
# Serializer validates
# View sets author automatically
# Serializer saves
# Model stores it
# You’re seeing the separation of responsibility in action.




