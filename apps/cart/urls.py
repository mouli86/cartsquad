from django.contrib import admin
from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('view/<int:user_id>/', views.view_cart, name='view_cart'),
    path('delete/<int:product_id>/<int:user_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('add_to_cart/<int:prod_id>/<int:user_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart')]
