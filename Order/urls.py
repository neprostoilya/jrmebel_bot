from django.urls import path
from Order.views import OrderAPIView, CreateOrderAPIView

app_name = 'Order'

urlpatterns = [
    path('my_order/<user>', OrderAPIView.as_view()),
    path('create_order/', CreateOrderAPIView.as_view()),
]