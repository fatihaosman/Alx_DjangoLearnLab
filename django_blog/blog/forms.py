from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models  import Post

  # We are EXTENDING Django's default registration form
  # This form already has: username, password1, password2
class RegisterForm(UserCreationForm):
    # Add email field on top of default UserCreationForm
     # We add an extra field that Django did not include by default
    email = forms.EmailField(required=True)
#This form belongs to the User table”
#“Only show these columns as form inputs”
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# UserCreationForm already handles:

# password validation

# password hashing

# We extend it, not rewrite it

# Meta tells Django:

# which model we are working with

# which fields to show


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']