from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Vote
from .serializers import VoteSerializer

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        post_id = request.data.get("post")
        vote_type = int(request.data.get("vote_type"))
        user = request.user if request.user.is_authenticated else None

        vote = Vote.objects.filter(post_id=post_id, user=user).first()

        # 🔽 DOWNVOTE LOGIC
        if vote_type == -1:
            if vote:
                if vote.vote_type == 1:
                    vote.delete()   # +1 → 0
                    return Response({"message": "Upvote removed"}, status=200)
                
                # already 0 or -1 → do nothing
                return Response({"message": "No change"}, status=200)

            # no vote → do nothing
            return Response({"message": "No change"}, status=200)

        # 🔼 UPVOTE LOGIC
        if vote_type == 1:
            if vote:
                if vote.vote_type == 1:
                    return Response({"message": "Already upvoted"}, status=200)
                
                # if somehow -1 exists → convert to +1
                vote.vote_type = 1
                vote.save()
                return Response({"message": "Vote updated"}, status=200)

            # first time upvote
            Vote.objects.create(
                post_id=post_id,
                vote_type=1,
                user=user
            )
            return Response({"message": "Upvoted"}, status=201)