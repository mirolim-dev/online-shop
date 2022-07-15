from django.db.models import fields
from django import forms
from . import models
 
 
class UserAddressForm(forms.ModelForm):
    class Meta:
        model = models.UserAddress
        fields = ['is_active', 'country', 'city', 'street', 'building', 'apartment', 'floor']
 
    
class UserInfoForm(forms.ModelForm):   
    class Meta:
        model = models.UserInfo
        fields = ['first_name', 'last_name', 'image', 'username', 'email', 'zip', 'phone']
