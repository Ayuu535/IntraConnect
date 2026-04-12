from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
from IntraConnect.backend.posts.models import Post

class UserProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_pic', 'posts']

from IntraConnect.backend.posts.serializers import PostSerializer

def get_posts(self, obj):
    posts = Post.objects.filter(user=obj)
    return PostSerializer(posts, many=True).data