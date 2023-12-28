from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_or_eror

from Order.models import Orders
from Order.serializers import OrdersSerializer

class GetOrderAPIView(APIView):
    """
    View Get Order
    """

    def get(self, request, user, furniture_pk, description, status, completed):
        """
        Get Categories
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
            return Response(data=serialized_data, status=status_or_eror.HTTP_200_OK)
        else:
            return Response(data="No data found", status=status_or_eror.HTTP_404_NOT_FOUND)
        
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
            return Response(data=serializer.data, status=status_or_eror.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status_or_eror.HTTP_400_BAD_REQUEST)
    
class PutOrderAPIView(APIView):
    """
    View Put Order
    """

    def put(self, request, pk):
        """
        Put Order
        """
        data = request.data            
        instance = Orders.objects.get(
            pk=pk
        ) 
        serializer = OrdersSerializer(instance, data=data)   
        if serializer.is_valid():
            serializer.save()  
            return Response(data=serializer.data, status=status_or_eror.HTTP_200_OK)
        return Response(data=serializer.errors, status=status_or_eror.HTTP_400_BAD_REQUEST)
