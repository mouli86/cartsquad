from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('add', views.add_product, name='add_product'),
    path('edit/<int:id>', views.update_product, name='edit_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('view/<int:id>', views.view_product, name='view_product'),
    path('view_all', views.view_all_products, name='view_all'),
    path('search', views.search_products, name='search_'),
    path('', views.view_all_products, name='view_all')
    ]
