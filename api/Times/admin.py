from django.contrib import admin
from Times.models import Times


@admin.register(Times)
class TimesAdmin(admin.ModelAdmin):
    """
    Times 
    """
    list_display = ('pk', 'time', 'day')
    list_display_links = ('pk', )

