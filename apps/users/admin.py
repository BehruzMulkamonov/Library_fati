from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('date_joined', 'is_staff', 'is_active')
