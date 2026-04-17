from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from communities.models import Community   # 👈 ADD THIS

class PostPagination(PageNumberPagination):
    page_size = 10

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        return (
            Post.objects
            .select_related('user', 'community')
            .annotate(
                vote_score=Sum('votes__vote_type'),
                comment_count=Count('comments')
            )
            .order_by('-created_at')
        )

    # ✅ FIX HERE
    def perform_create(self, serializer):
        community = Community.objects.first()

        if not community:
            raise Exception("No community exists")

        serializer.save(
            user=self.request.user,
            community=community
        )

def get_posts(request):
    posts = Post.objects.all().annotate(
        vote_score=Coalesce(Sum('votes__vote_type'), 0),
        comment_count=Count('comments')
    )
    
    return Response(PostSerializer(posts, many=True).data)

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().annotate(
            vote_score=Coalesce(Sum('votes__vote_type'), 0),
            comment_count=Count('comments')
        )
