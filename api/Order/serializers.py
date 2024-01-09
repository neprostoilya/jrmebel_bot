from rest_framework import serializers
from Order.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = ('pk', 'user', 'furniture', 'description', 'status', 'completed', 
            'get_title_furniture_ru','get_title_furniture_uz', 'get_description_furniture_ru', 
            'get_description_furniture_uz', 'get_category_furniture_ru', 'get_category_furniture_uz',
            'get_style_furniture_ru', 'get_style_furniture_uz', 'datetime_order'
        )
        
    def create(self, validated_data):
        return super().create(validated_data)
