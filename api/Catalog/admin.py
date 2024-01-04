from django.contrib import admin
from Catalog.models import Categories, Styles, Gallery, Furnitures

class GalleryInline(admin.TabularInline):
    """
    Gallery Images
    """
    fk_name = 'furniture'
    model = Gallery
    extra = 1

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Categories 
    """
    list_display = ('pk', 'title_ru', 'subcategory')
    list_editable = ('subcategory',)
    list_display_links = ('pk', 'title_ru',)

@admin.register(Styles)
class StylesAdmin(admin.ModelAdmin):
    """
    Styles 
    """
    list_display = ('pk', 'title_ru',)
    list_display_links = ('pk', 'title_ru',)

@admin.register(Furnitures)
class FurnituresAdmin(admin.ModelAdmin):
    """
    Furniture 
    """
    list_display = ('pk', 'title_ru','descriptiontrim', 'category', 'style', 'price','img_preview')
    list_display_links = ('pk', 'title_ru',)
    list_editable = ('category', 'style', 'price')
    inlines = (GalleryInline,)