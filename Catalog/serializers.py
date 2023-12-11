from rest_framework import serializers
from Catalog.models import Categories, Styles, Furnitures

class CategoriesSerializer(serializers.ModelSerializer):
    """
    Categories Serializer
    """
    class Meta:
        model = Categories
        fields = ('pk', 'title', 'subcategory')

class StylesSerializer(serializers.ModelSerializer):
    """
    Styles Serializer
    """
    class Meta:
        model = Styles
        fields = ('pk', 'title')

class FurnituresSerializer(serializers.ModelSerializer):
    """
    Furnitures Serializer
    """
    class Meta:
        model = Furnitures
        fields = ('pk', 'title', 'subcategory', 'image', 'description', 'category', 'style')

