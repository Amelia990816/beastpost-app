from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('store_name', 'user__username', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Store Information', {'fields': ('user', 'store_name', 'description')}),
        ('Status', {'fields': ('is_active',)}),
        ('Timestamps', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields