from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404





from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from posts.serializers import PostSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
#We use APIView because login needs custom logic.
# It:
# Validates data
# Returns token + user

class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
# This means:
# ❌ No token → Access denied
# ✅ Valid token → Access granted
    def get_object(self):
        return self.request.user   #"Give me the currently logged-in user."
      
      


class FollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = self.get_queryset().get(id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.email}"})

class UnfollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = self.get_queryset().get(id=user_id)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.email}"})
      
      


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all posts from users that the current user follows
        followed_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)