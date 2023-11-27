from django.contrib import admin
from django.urls import path
from . import views

# Define the namespace for the 'orders' app.
app_name = 'orders'

# Define URL patterns for the 'orders' app.
urlpatterns = [
    path('view_order/<str:order_id>/', views.view_order, name='view_order'),
    path('checkout/<int:cart_id>/', views.checkout, name='checkout_shared_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history/', views.view_order_history, name='order_history'),
]
