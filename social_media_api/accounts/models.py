from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
      
      
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