from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Vote
from IntraConnect.backend.posts.models import Post

class VoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        vote_type = request.data.get('vote_type')

        if vote_type not in [1, -1]:
            return Response({'error': 'Invalid vote'}, status=400)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        vote, created = Vote.objects.get_or_create(user=user, post=post)

        # 🔥 LOGIC STARTS HERE

        if not created:
            if vote.vote_type == vote_type:
                vote.delete()
                return Response({'message': 'Vote removed'})
            else:
                vote.vote_type = vote_type
                vote.save()
                return Response({'message': 'Vote updated'})

        vote.vote_type = vote_type
        vote.save()

        return Response({'message': 'Vote added'})