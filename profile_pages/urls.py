from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.profile_main_view, name='profile-main'),
   
    path('address/', views.profile_address_view, name='profile-address'),
    path('wishlist/', views.profile_wishlist_view, name='profile-wishlist'),
    path('setting/', views.profile_setting_view, name='profile-setting'),
    # path('seller/', views.profile_seller_view, name='profile-seller'),
    
    path('add-address/', views.add_profile_address, name='add_profile_address'),
    path('address/update/<int:pk>/', views.update_profile_address, name='update_address'),
    path('address/delete/<int:pk>/', views.delete_address, name='delete_address'),
    path('address/active/<int:pk>/', views.make_default, name='make_default'),
    # path('address/disactive/<int:pk>/', views.out_of_default, name='out_of_default'),
]
