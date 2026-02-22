from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like
from notifications.models import Notification


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Correct version without commas
        post = generics.get_object_or_404(post, pk=pk)
        Like.objects.get_or_create(user=request.user, post=post)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
    
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # This one is WRONG (has commas)
        post = generics.get_object_or_404(Post, pk=pk),
        Like.objects.get_or_create(user=request.user, post=post),
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)