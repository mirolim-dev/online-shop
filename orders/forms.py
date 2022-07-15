from django import forms
from django.forms import ModelForm, fields
from .models import CartModel, Order

class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']