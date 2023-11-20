from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='index'),
    path('add/<int:product_id>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('view/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>', views.update_quantity, name='update_quantity'),
]