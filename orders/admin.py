from django.contrib import admin
from . import models
# Register your models here.
class CarttAdmin(admin.ModelAdmin):
    
    list_display = ['user', 'product', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name', 'last_name', 'phone', 'status', 'ordered_at', 'updated_at']
    search_fields = [ 'id', 'status', 'first_name', 'last_name', 'email' ]
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id','product', 'quantity', 'added_at'] 
    search_fields = ['order_id']
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.CartModel, CarttAdmin)

