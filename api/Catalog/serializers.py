from rest_framework import serializers
from Catalog.models import Categories, Styles, Furnitures, Gallery

class CategoriesSerializer(serializers.ModelSerializer):
    """
    Categories Serializer
    """
    class Meta:
        model = Categories
        fields = ('pk', 'title_ru', 'title_uz', 'subcategory', 'without_style')

class StylesSerializer(serializers.ModelSerializer):
    """
    Styles Serializer
    """
    class Meta:
        model = Styles
        fields = ('pk', 'title_ru', 'title_uz', 'category')

class FurnituresSerializer(serializers.ModelSerializer):
    """
    Furnitures Serializer
    """
    class Meta:
        model = Furnitures
        fields = (
            'pk', 'title_ru', 'title_uz', 'category', 'image', 'description_ru', 
            'description_uz', 'style', 'get_category_title_uz', 'get_category_title_ru',
            'get_style_title_ru', 'get_style_title_uz', 'price'
        )

class GallerySerializer(serializers.ModelSerializer):
    """
    Gallery Serializer
    """
    class Meta:
        model = Gallery
        fields = ('pk', 'image', 'furniture')

