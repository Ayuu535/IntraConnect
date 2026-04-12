from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class PostPagination(PageNumberPagination):
    page_size = 10   # number of posts per request

from django.db.models import Sum, Count

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
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)