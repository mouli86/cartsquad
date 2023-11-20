from django.contrib import admin
from django.urls import path
from . import views

# Define the namespace for the 'orders' app.
app_name = 'orders'

# Define URL patterns for the 'orders' app.
urlpatterns = [
    path('view_order_history/<int:user_id>', views.view_order_history, name='view_order_history'),
    path('checkout/', views.checkout, name='checkout'),
]
