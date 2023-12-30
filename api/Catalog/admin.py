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
    list_display = ('pk', 'title', 'subcategory')
    list_editable = ('subcategory',)
    list_display_links = ('pk', 'title',)

@admin.register(Styles)
class StylesAdmin(admin.ModelAdmin):
    """
    Styles 
    """
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)

@admin.register(Furnitures)
class FurnituresAdmin(admin.ModelAdmin):
    """
    Furniture 
    """
    list_display = ('pk', 'title','descriptiontrim', 'category', 'style', 'price','img_preview')
    list_display_links = ('pk', 'title',)
    list_editable = ('category', 'style', 'price')
    inlines = (GalleryInline,)