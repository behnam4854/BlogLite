from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """For modify user model and control login and signup option"""

    class Meta:
        model = User
        fields = ['url', 'username','first_name', 'email', 'password','is_staff',]

        extra_kwargs = {
            "password": {"write_only": True},
        }

class PostSerializer(serializers.ModelSerializer):
    """for managing update, create and delete post"""

    class Meta:
        model = Post
        fields = ['id','title', 'content']