from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    # Many-to-many self-relationship for following users
    following = models.ManyToManyField(
        'self', 
        symmetrical=False,   # Direction matters: A follows B != B follows A
        related_name='followers',  # Reverse relation: who follows this user
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
      
      
# It means:
  # followers = models.ManyToManyField(
  #       'self',
  #       symmetrical=False,
  #       related_name='following',
  #       blank=True
  #   )

# A user can follow many users
# A user can have many followers
# 'self' → The relationship is with the same model (User)
# symmetrical=False → If I follow you, you don’t automatically follow me
# Exactly how Instagram works.




# 'rest_framework.authtoken'

# Why?
# When a user logs in:
# They receive a token
# They send this token with every request
# The API checks if the token is valid
# Instead of sessions (used in normal websites),
# APIs use tokens.