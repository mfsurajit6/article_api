from django.urls import path

from article.views import ArticleGenericView, ArticleOpAPIView

urlpatterns = [
    path('', ArticleGenericView.as_view()),
    path('<int:id>/', ArticleGenericView.as_view()),
    path('add/', ArticleOpAPIView.as_view()),
    path('update/<int:id>/', ArticleOpAPIView.as_view()),
    path('delete/<int:id>/', ArticleOpAPIView.as_view()),
    
]
