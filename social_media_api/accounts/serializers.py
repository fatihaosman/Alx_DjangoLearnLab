from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model() #returns the active user taht was defined in : 
# AUTH_USER_MODEL = 'accounts.User'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Controls how the password field behaves in API responses.   password is write-only, meaning it can be used to create or update a user but will not be included in API responses. This is a security measure to prevent exposing sensitive information.
        # extra_kwargs is your serializer automatically including 
        #         {
        #   "username": "john",
        #   "email": "john@email.com",
        #   "password": "123456"
        # }
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)  #This creates a token for that user.
        return user   #This creates a token for that user.

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)  #Does this username/password exist?
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        token, created = Token.objects.get_or_create(user=user)
        return {
            "user": UserSerializer(user).data,
            "token": token.key
        }   #So login = verify + return token.