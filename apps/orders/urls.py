from django.contrib import admin
from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('view_order_history/<int:user_id>/', views.view_order_history, name='view_order_history'),
    path('add_to_orders/<int:user_id>/<int:order_id>/', views.add_to_orders, name='add_to_orders'),
]