from django.db import models
from django.contrib.auth.models import User  # Django's built-in user model


class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)

    # Main content/body of the blog post
    content = models.TextField()

    # Date when the post is created
    #Automatically saves the date when post is created
    #You don’t need to manually set it when creating a new post
    published_date = models.DateTimeField(auto_now_add=True)

    # Author of the post (one user can have many posts)
    author = models.ForeignKey(   User,    on_delete=models.CASCADE
          #Links a post to a user,  one user can have many posts
      #If user is deleted → their posts are deleted too
      
      #    related_name='posts'
       # allows: user.posts.all() to get all posts by that user
    )

    def __str__(self):
        # This controls how the post appears in admin and shell
        return self.title
