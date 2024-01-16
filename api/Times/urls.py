from django.urls import path
from Times.views import GetTimesAPIView

app_name = 'Times'

urlpatterns = [
    path('get_times/<day>/', GetTimesAPIView.as_view()),
]