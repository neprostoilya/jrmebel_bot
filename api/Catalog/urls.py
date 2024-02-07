from django.urls import path

from Catalog.views import CategoriesAPIView, SubcategoriesAPIView, \
    StylesAPIView, FurnituresAPIView, GalleryAPIView, GetFurnitureAPIView, GetFurnituresByCategoryAPIView


app_name = 'Catalog'

urlpatterns = [
    path('get_categories/', CategoriesAPIView.as_view()),
    path('get_subcategories/<category>/', SubcategoriesAPIView.as_view()),
    path('get_styles/<category>/', StylesAPIView.as_view()),
    path('get_furnitures/<category>/<style>/', FurnituresAPIView.as_view()),
    path('get_furnitures_by_category/<category>/', GetFurnituresByCategoryAPIView.as_view()),
    path('get_furniture/<pk>/', GetFurnitureAPIView.as_view()),
    path('get_gallery/<furniture>/', GalleryAPIView.as_view()),
]