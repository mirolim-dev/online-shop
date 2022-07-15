from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

   
    
class Product_Image_Admin(admin.StackedInline):
    model = models.Product_images
    fields = ["image"]
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price', 'subcategory']
    search_fields = [ 'name' ]
    prepopulated_fields = {
        'slug': ('name',)
    }

    inlines = [Product_Image_Admin]

admin.site.register(models.CategoryModel, CategoryAdmin)
admin.site.register(models.SubcategoryModel, SubcategoryAdmin)
admin.site.register(models.ProductModel,ProductAdmin)