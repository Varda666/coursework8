from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_role', 'email', 'name', 'last_login',
                    'is_staff', 'is_active')
    list_filter = ('user_role', 'email', 'name', 'last_login',
                   'is_staff', 'is_active')
    search_fields = ('user_role', 'email', 'name', 'last_login',
                     'is_staff', 'is_active')


