from django.contrib import admin
from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_vendor', 'phone_number', 'date_joined')
    list_filter = ('is_vendor', 'date_joined')
    search_fields = ('username', 'email', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email', 'first_name', 'last_name', 'phone_number')}),
        ('Account Status', {'fields': ('is_active', 'is_vendor', 'is_staff', 'is_superuser')}),
        ('Timestamps', {'fields': ('date_joined', 'last_login'), 'classes': ('collapse',)}),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')
    search_fields = ('user__username', 'address')
    readonly_fields = ('user',)
    fieldsets = (
        ('User Profile', {'fields': ('user',)}),
        ('Details', {'fields': ('bio', 'avatar', 'address')}),
    )