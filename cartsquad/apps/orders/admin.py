from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'order_total', 'order_date_created', 'delivered')
    readonly_fields = ('order_id', 'order_date_created')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Orders, name = 'Order', admin_class = OrdersAdmin)

