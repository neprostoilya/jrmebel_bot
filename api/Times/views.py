from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Times.models import Times
from Times.serializers import TimesSrializer


class GetTimesAPIView(APIView):
    """
    Get Times
    """
    model = Times
    serializer_class = TimesSrializer

    def get(self, request, day):
        model = self.model.objects.filter(
            day=day
        )
        serializer = self.serializer_class(model, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)