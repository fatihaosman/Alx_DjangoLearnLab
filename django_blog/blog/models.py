from django.db import models
from django.contrib.auth.models import User  # Django's built-in user model


from django.utils import timezone

# tag model structure.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Explanation
# name → stores tag name (e.g. "django", "python")
# unique=True → prevents duplicate tags
# __str__ → makes admin readable

class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)

    # Main content/body of the blog post
    content = models.TextField()

    # Date when the post is created
    #Automatically saves the date when post is created
    #You don’t need to manually set it when creating a new post
    published_date = models.DateTimeField(auto_now_add=True)

    # Auth
    # 
    # or of the post (one user can have many posts)
    author = models.ForeignKey(   User,    on_delete=models.CASCADE
          #Links a post to a user,  one user can have many posts
      #If user is deleted → their posts are deleted too
      
      #related_name='posts'
       # allows: user.posts.all() to get all posts by that user
    )
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    

    def __str__(self):
        # This controls how the post appears in admin and shell
        return self.title
      
      
     
# comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'





