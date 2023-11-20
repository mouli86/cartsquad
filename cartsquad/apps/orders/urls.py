from django.contrib import admin
from django.urls import path
from . import views

# Define the namespace for the 'orders' app.
app_name = 'orders'

# Define URL patterns for the 'orders' app.
urlpatterns = [
    # URL pattern for viewing order history, using the user_id as a parameter.
    path('view_order_history/<int:user_id>/', views.view_order_history, name='view_order_history'),

    # URL pattern for adding to orders, using user_id and order_id as parameters.
    path('add_to_orders/<int:user_id>/<int:order_id>/', views.add_to_orders, name='add_to_orders'),
]
