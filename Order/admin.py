from django.contrib import admin
from Order.models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """
    Orders 
    """
    list_display = ('pk', 'user', 'furniture', 'descriptiontrim', 'material', 'color', 'size', 'img_preview')
    list_display_links = ('pk', 'user', 'furniture',)
