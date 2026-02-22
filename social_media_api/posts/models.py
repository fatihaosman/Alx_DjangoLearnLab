from django.db import models
from django.contrib.auth import get_user_model

# This ensures we use the active User model (default or custom)
User = get_user_model()


class Post(models.Model):
    # The user who created the post
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If user is deleted, delete their posts
        related_name='posts'       # Allows user.posts.all()
    )

    # Title of the post
    title = models.CharField(max_length=255)

    # Main content
    content = models.TextField()

    # Automatically set when created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically update when modified
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Which post this comment belongs to
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'   # Allows post.comments.all()
    )

    # Who wrote the comment
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username}"
      
from django.conf import settings

class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.email} likes {self.post.title}"      
      

# Model defines structure

# ForeignKey creates relationships

# related_name allows reverse access