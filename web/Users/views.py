from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from Users.models import UserProfile
from Users.serializers import RegistrationSerializer, LoginSerializer, UserSerializer

class UserAPIView(APIView):
    """
    Get User
    """
    serializer_class = UserSerializer

    def get(self, request):
        """
        Get Users
        """
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    """
    Create User
    """
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)