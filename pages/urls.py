from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blank/', views.blank_starter, name='blank-starter'),
    path("search/", views.search_view, name="searched_page"),
]
