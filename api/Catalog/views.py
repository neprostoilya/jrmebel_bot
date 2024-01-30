from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Catalog.models import Categories, Styles, Furnitures, Gallery
from Catalog.serializers import CategoriesSerializer, \
    StylesSerializer, FurnituresSerializer, GallerySerializer
from Catalog.logics.view_logics import get_subcategories_by_category
    
class CategoriesAPIView(APIView):
    """
    View Categories
    """
    model = Categories
    serializer_class = CategoriesSerializer

    def get(self, request):
        categories = self.model.objects.all().filter(
            subcategory=None
        )

        serializer = self.serializer_class(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class SubcategoriesAPIView(APIView):
    """
    View Subcategories
    """
    serializer_class = CategoriesSerializer

    def get(self, request, category):
        subcategories = get_subcategories_by_category(
            category=category
        )

        serializer = self.serializer_class(subcategories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class StylesAPIView(APIView):
    """
    View Styles
    """
    model = Styles
    serializer_class = StylesSerializer

    def get(self, request, category):
        styles = self.model.objects.filter(
            category=category
        )

        serializer = self.serializer_class(styles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class FurnituresAPIView(APIView):
    """
    View Furnitures
    """
    model = Furnitures
    serializer_class = FurnituresSerializer

    def get(self, request, category, style):
        furnitures = self.model.objects.filter(
            category=category,
            style=style,
        )

        serializer = self.serializer_class(furnitures, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class GalleryAPIView(APIView):
    """
    View Gallery
    """
    model = Gallery
    serializer_class = GallerySerializer

    def get(self, request, furniture):
        furnitures = self.model.objects.filter(
            furniture=furniture
        )

        serializer = self.serializer_class(furnitures, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class GetFurnitureAPIView(APIView):
    """
    Get Furniture by pk
    """
    model = Furnitures
    serializer_class = FurnituresSerializer

    def get(self, request, pk):
        furniture = self.model.objects.filter(
            pk=pk
        )
        
        serializer = self.serializer_class(furniture, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
