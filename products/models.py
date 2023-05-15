from django.db import models
from django.db.models.fields.related import ForeignKey

# import products

# Create your models here.

class CategoryModel(models.Model):
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
        
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to = 'category/', null=True)
    shortly_description = models.CharField(max_length=250, blank=True, null=True)
    shortly_comment = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class SubcategoryModel(models.Model):
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        
        
    category_name = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    category_slug = models.CharField(max_length = 250, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=150, null=True)
    slug = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to = 'subcategory/', null=True)
    
    def __str__(self):
        return self.name
 

    
class ProductModel(models.Model):
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    # Foreign keys
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubcategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True)
    subcategory_slug = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    price = models.FloatField(null=True)
    old_price = models.FloatField(blank=True, null=True)
    description = models.TextField(null=True)
    color = models.CharField(max_length=80, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    guaranty = models.CharField(max_length=80, null=True, blank=True)
    manufacture = models.CharField(max_length=300, null=True, blank=True)
   
    def __str__(self):
        return self.name
    
class Product_images(models.Model):
    image = models.ImageField(upload_to='product/inlines/', null=True)  
    product = ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_images", null=True)  