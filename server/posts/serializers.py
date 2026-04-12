from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    vote_score = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'