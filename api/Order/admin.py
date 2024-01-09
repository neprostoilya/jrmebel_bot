from django.contrib import admin
from Order.models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """
    Orders 
    """
    list_display = ('pk', 'user', 'furniture', 'descriptiontrim', 'status', 'completed', 'datetime_order')
    list_display_links = ('pk', )
