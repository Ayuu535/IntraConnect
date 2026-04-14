from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import User
from .serializers import UserProfileSerializer
from rest_framework import generics
from .serializers import RegisterSerializer


# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"}, status=201)



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer



class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)