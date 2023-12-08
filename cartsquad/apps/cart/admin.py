from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'cart_owner_id', 'cart_status', 'shared_cart', 'cart_date_created')
    readonly_fields = ('cart_id', 'cart_owner_id', 'cart_status', 'cart_products', 'cart_total')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cart, CartAdmin)
# Register your models here.

