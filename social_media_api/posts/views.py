from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    Only the author can edit or delete.
    Others can only read.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow editing if user is the author
        return obj.author == request.user
      
class PostViewSet(viewsets.ModelViewSet):
    """
    Provides:
    - list
    - retrieve
    - create
    - update
    - delete
    automatically
    """

    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set author as logged-in user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(
            author__in=followed_users
        ).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)