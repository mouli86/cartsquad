from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [  
    path('register/user', views.customer_register, name = 'customer_register'),
    path('register/retailer', views.retailer_register, name = 'retailer_register'),
    path('logout', views.logout_user, name = 'logout'),
    path('login/user', views.user_login_view, name = 'user_login'),
    path('login/register', views.retailer_login_view, name = 'retailer_login')
]
