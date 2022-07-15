from django.contrib import admin
from . import models

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'city', 'is_active']
    search_fields = ['country', 'city']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone', 'image']
    search_fields = ['username', 'first_name', 'last_name', 'phone']

admin.site.register(models.UserAddress, AddressAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.Default_avatar)