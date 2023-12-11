from rest_framework import serializers
from Order.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = ('pk', 'user', 'furniture', 'category', 'style',
                 'size', 'color', 'image', 'material', 'text')
    
    def create(self, validated_data):
        return super().create(validated_data)