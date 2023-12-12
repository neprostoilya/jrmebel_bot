from django.contrib import admin
from Order.models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """
    Orders 
    """
    list_display = ('pk', 'user', 'furniture', 'material',
                    'color', 'size', 'descriptiontrim', 'status', 'completed', 'date_to', 'img_preview')
    list_display_links = ('pk', )
