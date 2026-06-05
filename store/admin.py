from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Shop, Category, Product


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra', {'fields': ('avatar', 'bio')}),
    )


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'created_at', 'slug')
    prepopulated_fields = {}
    search_fields = ('name', 'owner__username')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'price', 'in_stock', 'created_at')
    list_filter = ('in_stock', 'categories', 'shop')
    search_fields = ('name',)
    filter_horizontal = ('categories',)
