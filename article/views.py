from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework import status
from rest_framework.fields import REGEX_TYPE
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from article.serializer import ArticleSerializer
from article.models import Article
from user.models import User


class ArticleGenericView(GenericAPIView, RetrieveModelMixin, ListModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
class ArticleOpAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_user(self, token):
        try:
            user_id = Token.objects.get(key=token).user_id
            return user_id
        except User.DoesNotExist:
            return None

    def get_article(self, id):
        try:
            return Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return None


    def post(self, request):
        token = request.auth.key
        user = self.get_user(token)

        article = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "author": user
        }
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        token = request.auth.key
        user = self.get_user(token)
        article = self.get_article(id)

        if not user :
            return Response({"msg":"Invalid Token"}, status=status.HTTP_404_NOT_FOUND)
        if not article:
            return Response({"msg":"Article Does not exixts"}, status=status.HTTP_404_NOT_FOUND)

        if user == article.author_id:
            article_new = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "author": user
            }
            serializer = ArticleSerializer(article, data=article_new)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id):
        token = request.auth.key
        user = self.get_user(token)
        article = self.get_article(id)

        if not user :
            return Response({"msg":"Invalid Token"}, status=status.HTTP_404_NOT_FOUND)
        if not article:
            return Response({"msg":"Article Does not exixts"}, status=status.HTTP_404_NOT_FOUND)

        if user == article.author_id:
            article.delete()
            return Response({"msg": "Article Deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN)
