from django.contrib import admin

from apps.account.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'user_type', 'created', 'updated')
    search_fields = ('get_full_name', 'email',)
    list_filter = ('user_type',)