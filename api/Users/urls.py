from django.urls import path

from Users.views import RegisterAPIView, LoginAPIView, \
    UserAPIView


app_name = 'Users'

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]