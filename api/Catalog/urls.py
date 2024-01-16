from django.urls import path

from Catalog.views import CategoriesAPIView, SubcategoriesAPIView, \
    StylesAPIView, FurnituresAPIView, GalleryAPIView, GetFurnitureAPIView


app_name = 'Catalog'

urlpatterns = [
    path('get_categories/', CategoriesAPIView.as_view()),
    path('get_subcategories/<category>/', SubcategoriesAPIView.as_view()),
    path('get_styles/', StylesAPIView.as_view()),
    path('get_furnitures/<category>/<style>/', FurnituresAPIView.as_view()),
    path('get_furniture/<pk>/', GetFurnitureAPIView.as_view()),
    path('get_gallery/<furniture>/', GalleryAPIView.as_view()),
]