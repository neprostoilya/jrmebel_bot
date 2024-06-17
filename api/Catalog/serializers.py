from rest_framework import serializers
from Catalog.models import Categories, Styles, Furnitures, Gallery

class CategoriesSerializer(serializers.ModelSerializer):
    """
    Categories Serializer
    """
    class Meta:
        model = Categories
        fields = ('pk', 'title',  'subcategory', 'without_style')

class StylesSerializer(serializers.ModelSerializer):
    """
    Styles Serializer
    """
    class Meta:
        model = Styles
        fields = ('pk', 'title',  'category')

class FurnituresSerializer(serializers.ModelSerializer):
    """
    Furnitures Serializer
    """
    class Meta:
        model = Furnitures
        fields = (
            'pk', 'title',  'category', 'image', 'description', 
             'style', 'get_category_title',
            'get_style_title', 'price'
        )

class GallerySerializer(serializers.ModelSerializer):
    """
    Gallery Serializer
    """
    class Meta:
        model = Gallery
        fields = ('pk', 'image', 'furniture')

