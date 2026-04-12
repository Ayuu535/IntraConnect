from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.serializers import PostSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_pic', 'posts']

    def get_posts(self, obj):
        posts = Post.objects.filter(user=obj)
        return PostSerializer(posts, many=True).data