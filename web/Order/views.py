from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Order.serializers import OrdersSerializer
from Order.logics.view_logics import get_orders

class OrderAPIView(APIView):
    """
    View Order
    """

    def get(self, request, user):
        """
        Get Categories
        """
        serializer = OrdersSerializer(get_orders(user), many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class CreateOrderAPIView(APIView):
    """
    View Create Order
    """

    def post(self, request):
        """
        Create Order
        """
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)