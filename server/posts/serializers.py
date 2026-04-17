from rest_framework import serializers
from .models import Post
from django.db.models import Sum

class PostSerializer(serializers.ModelSerializer):
    vote_score = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["user", "community", "created_at"]

    def get_vote_score(self, obj):
        return obj.votes.aggregate(score=Sum("vote_type"))["score"] or 0

    def get_comment_count(self, obj):
        return obj.comments.count()
