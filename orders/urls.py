from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.offer_view, name='offers'), 
    
    path('payment/', views.payment_view, name='payment'),
    
    path('shopping-cart/', views.shopping_cart_view, name='shop-cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:pk>/', views.delete_from_cart, name='delete-from-cart'),
    path('plus-cart-item/<int:c_pk>', views.plus_cart_item, name='plus_product_quantity'),
    path('minus_cart_item/<int:c_pk>', views.minus_cart_item, name='minus_cart_item'),
    
    path('order/', views.profile_order_view, name='profile-orders'),
    path('add-to-order/<str:data>', views.add_to_order, name='add_to_order'),
    
    path("wishlist/<int:pk>/<str:data>", views.add_to_wishlist, name="add-to-wishlist"),
    path("wishlist-delete/<int:pk>/<str:data>", views.delete_from_wishlist, name="delete_from_wishlist")
]
