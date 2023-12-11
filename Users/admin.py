from django.contrib import admin
from Users.models import UserProfile

@admin.register(UserProfile)
class  UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'phone', 'telegram_pk', 'is_staff', 'is_admin')
    list_editable = ('is_staff', 'is_admin')
    list_display_links = ('username',)