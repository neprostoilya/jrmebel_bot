from rest_framework import serializers
from Times.models import Times


class TimesSrializer(serializers.ModelSerializer):
    """
    Times Serializer
    """

    class Meta:
        model = Times
        fields = ('pk', 'time', 'day')