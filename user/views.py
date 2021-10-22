from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = authenticate(email=email, password=password)
            token = Token.objects.get_or_create(user = user)
            return Response({'token' : str(token[0]), 'id': user.id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': "Invalid Credentials"}, status = status.HTTP_400_BAD_REQUEST)

class LogOutAPIView(APIView):
    def post(self, request):
        token = request.auth.key 
        # print(token)
        # user = Token.objects.get(key=token).user_id
        # print(user)
        Token.objects.filter(key=token).delete()
        return Response({'message': 'Logged Out'})


