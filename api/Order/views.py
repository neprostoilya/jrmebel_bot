from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Order.models import Orders
from Order.serializers import OrdersSerializer


class GetOrdersByUserAPIView(APIView):
    """
    View Get Orders User
    """
    model = Orders
    serializer_class = OrdersSerializer

    def get(self, request, user):
        orders = self.model.objects.filter(
            user=user, 
        )

        if orders.exists():
            serializer = self.serializer_class(orders, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GetOrderAPIView(APIView):
    """
    View Get Order
    """
    model = Orders
    serializer_class = OrdersSerializer

    def get(self, request, user, furniture_pk, description, status_order, datetime_order):

        order = self.model.objects.filter(
            user=user, 
            furniture=furniture_pk, 
            description=description, 
            status=status_order, 
            datetime_order=datetime_order
        )

        if order.exists():
            serializer = self.serializer_class(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CreateOrderAPIView(APIView):
    """
    View Create Order
    """
    serializer_class = OrdersSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOrderByPkAPIView(APIView):
    """
    View Get Order by pk
    """
    model = Orders
    serializer_class = OrdersSerializer

    def get(self, request, order_pk):
        order = self.model.objects.filter(
            pk=order_pk
        )

        if order.exists():
            serializer = self.serializer_class(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UpdateOrderAPIView(APIView):
    """
    View Put Order
    """
    model = Orders
    serializer_class = OrdersSerializer

    def get(self, request, pk):
        order = get_object_or_404(self.model, pk=pk)

        serializer = self.serializer_class(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        order = get_object_or_404(self.model, pk=pk)

        serializer = self.serializer_class(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetOrderByDatetimeAPIView(APIView):
    """
    View Get Order by datetime
    """
    model = Orders
    serializer_class = OrdersSerializer

    def get(self, request, datetime):
        order = self.model.objects.filter(
            datetime_order=datetime
        )
        
        if order.exists():
            serializer = self.serializer_class(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)