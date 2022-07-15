from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>', views.categories_view, name='category'),
    path('detail-products/<slug:slug>', views.product_details, name='detail-product'),
    path('listing-large/<slug:slug>', views.listing_large_view, name='listing-large'),
   
]
 