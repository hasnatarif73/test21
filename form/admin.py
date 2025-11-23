from django.contrib import admin
from .models import userForm

@admin.register(userForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'job', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('job', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
