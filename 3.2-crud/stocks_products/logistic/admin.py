from django.contrib import admin

from logistic.models import Stock, StockProduct, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(StockProduct)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'price']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
