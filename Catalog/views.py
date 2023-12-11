from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Catalog.serializers import CategoriesSerializer, \
    StylesSerializer, FurnituresSerializer
from Catalog.logics.view_logics import get_categories, \
    get_all_styles, get_furniture_by_category_and_style, \
    get_subcategories_by_category

class CategoriesAPIView(APIView):
    """
    View Categories
    """

    def get(self, request):
        """
        Get Categories
        """
        serializer = CategoriesSerializer(get_categories, many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class SubcategoriesAPIView(APIView):
    """
    View Subcategories
    """

    def get(self, request, category):
        """
        Get Subcategories
        """
        serializer = CategoriesSerializer(get_subcategories_by_category(category), many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class StylesAPIView(APIView):
    """
    View Styles
    """

    def get(self, request):
        """
        Get Styles
        """
        serializer = StylesSerializer(get_all_styles, many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class FurnituresAPIView(APIView):
    """
    View Furnitures
    """

    def get(self, request, category, style):
        """
        Get Furnitures
        """
        serializer = FurnituresSerializer(get_furniture_by_category_and_style, many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer.data)