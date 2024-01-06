from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_or_erorr

from Order.models import Orders
from Order.serializers import OrdersSerializer

class GetOrdersByUserAPIView(APIView):
    """
    View Get Orders User
    """

    def get(self, request, user):
        """
        Get orders
        """
        orders = Orders.objects.filter(
            user=user, 
        )
        if orders.exists():
            serializer = OrdersSerializer(orders, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(status=status_or_erorr.HTTP_404_NOT_FOUND)

class GetOrderAPIView(APIView):
    """
    View Get Order
    """

    def get(self, request, user, furniture_pk, description, status, completed):
        """
        Get Order
        """
        order = Orders.objects.filter(
            user=user, 
            furniture=furniture_pk, 
            description=description, 
            status=status, 
            completed=completed
        )
        if order.exists():
            serializer = OrdersSerializer(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status_or_erorr.HTTP_404_NOT_FOUND)
        
class CreateOrderAPIView(APIView):
    """
    View Create Order
    """

    def post(self, request):
        """
        Create Order
        """
        data = request.data
        serializer = OrdersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status_or_erorr.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status_or_erorr.HTTP_400_BAD_REQUEST)

class GetOrderByPkAPIView(APIView):
    """
    View Get Order by pk
    """

    def get(self, request, order_pk):
        """
        Get Order by pk
        """
        order = Orders.objects.filter(
            pk=order_pk
        )
        if order.exists():
            serializer = OrdersSerializer(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status_or_erorr.HTTP_404_NOT_FOUND)

class UpdateOrderAPIView(APIView):
    """
    View Put Order
    """
    def get(self, request, pk):
        """
        Get Order by pk
        """
        order = get_object_or_404(Orders, pk=pk)
        serializer = OrdersSerializer(order)
        return Response(serializer.data, status=status_or_erorr.HTTP_200_OK)
    
    def put(self, request, pk):
        """
        Put Order
        """
        order = get_object_or_404(Orders, pk=pk)
        serializer = OrdersSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status_or_erorr.HTTP_200_OK)
        return Response(serializer.errors, status=status_or_erorr.HTTP_400_BAD_REQUEST)