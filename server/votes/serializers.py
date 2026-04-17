from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'post', 'vote_type']

    def create(self, validated_data):
        return Vote.objects.create(**validated_data)