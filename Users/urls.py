from django.urls import path
from .views import UserApiView

app_name = 'Users'

urlpatterns = [
    path('create/', UserApiView.as_view()),
]