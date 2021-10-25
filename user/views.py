from re import A
from django.shortcuts import render, resolve_url
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from user.serializers import UserSerializer
from user.models import User


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
    
class ProfileAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def get_user(self, token):
        try:
            user_id = Token.objects.get(key=token).user_id
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return Response({"msg":"Invalid Token"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        token = request.auth.key
        user = self.get_user(token)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        token = request.auth.key
        user = self.get_user(token)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        token = request.auth.key
        user = self.get_user(token)
        user.delete()
        return Response({"msg": "Account Deleted"}, status=status.HTTP_204_NO_CONTENT)



