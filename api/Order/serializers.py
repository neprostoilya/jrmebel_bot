from rest_framework import serializers
from Order.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = ('pk', 'user', 'furniture', 'description', 'status', 'datetime_order',
            'get_title_furniture', 'get_description_furniture', 
             'get_category_furniture', 
            'get_style_furniture', 
        )
        
    def create(self, validated_data):
        return super().create(validated_data)
