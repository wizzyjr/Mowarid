from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account  

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'first_name', 'room_number', 'last_name','last_login', 'phone_number', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'room_number')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)