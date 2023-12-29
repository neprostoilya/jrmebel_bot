from django.urls import path
from Order.views import GetOrderAPIView, CreateOrderAPIView, \
    PutOrderAPIView, OrdersAPIView

app_name = 'Order'

urlpatterns = [
    path('get_orders/<user>/', OrdersAPIView.as_view()),
    path('get_order/<user>/<furniture_pk>/<description>/<status>/<completed>/', GetOrderAPIView.as_view()),
    path('create_order/', CreateOrderAPIView.as_view()),
    path('put_order/<pk>/', PutOrderAPIView.as_view()),
]