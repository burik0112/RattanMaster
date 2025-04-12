from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import TransferToInventory, SizeModel, \
    CategoryModel, TransferFromInventory, ColorModel, InvoiceCreateModel, ProductEntry ,\
    RemaingInventoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TransferFromInventory)
class TransferFromInventoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TransferToInventory)
class TransferToInventoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(InvoiceCreateModel)
class InvoiceCreateModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'product_to', 'quantity', 'created_at']


@admin.register(ProductEntry)
class ProductEntryInventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'product_in', 'quantity', 'created_at']


@admin.register(RemaingInventoryModel)
class RemaingModelInventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'quantity']