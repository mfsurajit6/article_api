from django.urls import path

from .views import UserAPIView, LoginAPIView, LogOutAPIView, ProfileAPIView

urlpatterns = [
    path('signup/', UserAPIView.as_view()),
    path('signin/', LoginAPIView.as_view()),
    path('logout/', LogOutAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]
