from rest_framework import serializers
from Order.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = ('pk', 'user', 'furniture', 'material',
                    'color', 'size', 'descriptiontrim', 'status', 'completed', 'date_to', 'img_preview')
        
    def create(self, validated_data):
        return super().create(validated_data)