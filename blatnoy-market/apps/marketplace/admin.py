from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category', 'vendor', 'created_at')
    search_fields = ('title', 'description', 'vendor__store_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Product Information', {'fields': ('title', 'description', 'category')}),
        ('Pricing & Stock', {'fields': ('price', 'stock')}),
        ('Vendor', {'fields': ('vendor',)}),
        ('Media', {'fields': ('image',)}),
        ('Timestamps', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price', 'product')
    fields = ('product', 'price', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('user__username', 'stripe_charge_id')
    readonly_fields = ('created_at', 'stripe_charge_id')
    inlines = [OrderItemInline]
    fieldsets = (
        ('Customer', {'fields': ('user',)}),
        ('Order Details', {'fields': ('total_amount', 'is_paid')}),
        ('Payment', {'fields': ('stripe_charge_id',), 'classes': ('collapse',)}),
        ('Timestamps', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )