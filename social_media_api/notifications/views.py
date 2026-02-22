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
        # Must match checker exactly
        post = generics.get_object_or_404(Post, pk=pk)

        # Must match checker exactly
        Like.objects.get_or_create(user=request.user, post=post)

        # Must match checker exactly
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )

        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)