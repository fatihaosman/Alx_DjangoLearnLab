from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # Add email field on top of default UserCreationForm
    email = forms.EmailField(required=True)

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