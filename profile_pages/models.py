from decimal import MAX_EMAX
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAddress(models.Model):
    class Meta:
        verbose_name = 'User_address'
        verbose_name_plural = 'User_addresses'       
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=80)
    building = models.CharField(max_length=60, null=True, blank=True)
    apartment = models.CharField(max_length=12, null=True, blank=True)
    floor = models.CharField(max_length=4, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    # def __str__(self):
    #     return self.user 
    
class UserInfo(models.Model):
    class Meta:
        verbose_name = 'User_information'
        verbose_name_plural = 'User_informations'
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'profiles/', null=True, blank=True, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.zooniverse.org%2Fprojects%2Fpenguintom79%2Fpenguin-watch&psig=AOvVaw3znYM4x-Z6U1aNeuECcWYg&ust=1639545794567000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPjdrsbG4vQCFQAAAAAdAAAAABAH')
    username = models.CharField(max_length=50, null=True, help_text='username')
    email = models.EmailField()
    zip = models.IntegerField(help_text='enter your pochta code')
    phone = models.CharField(max_length=20, help_text='example:  +998991547854')
    
    def __str__(self):
        return self.username

class Default_avatar(models.Model):
    class Meta:
        verbose_name = 'default user avatar'
        verbose_name_plural = 'default user avatars'
    avatar = models.ImageField(upload_to = 'avatars/')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{ self.avatar.url }'
    