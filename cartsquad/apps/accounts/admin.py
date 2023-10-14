from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('user_id','email', 'first_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)

