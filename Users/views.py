from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Users.models import UserProfile
from Users.serializers import UserSerializer

class UserApiView(APIView):
    """
    Create User
    """
    serializer_class = UserSerializer

    def get(self, request):
        """
        Get Users
        """
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create User
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)