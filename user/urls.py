from django.urls import path

from .views import UserAPIView, LoginAPIView, LogOutAPIView

urlpatterns = [
    path('signup/', UserAPIView.as_view()),
    path('signin/', LoginAPIView.as_view()),
    path('logout/', LogOutAPIView.as_view()),
]
