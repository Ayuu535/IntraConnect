from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Community
from .serializers import CommunitySerializer

class CommunityListCreateView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)