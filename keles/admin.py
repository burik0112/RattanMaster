from django.contrib import admin

from keles.models import InvoiceCreateKeles, ProductEntryKeles, RemaingInventoryKeles


# Register your models here.


@admin.register(InvoiceCreateKeles)
class InvoiceCreateModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'product_to', 'quantity', 'created_at']


@admin.register(ProductEntryKeles)
class ProductEntryInventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'product_in', 'quantity', 'created_at']


@admin.register(RemaingInventoryKeles)
class RemaingModelInventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'color', 'quantity']