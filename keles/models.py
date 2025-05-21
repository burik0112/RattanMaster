from django.db import models
from django.utils import timezone

from index.models import CategoryModel, SizeModel, ColorModel, TransferToInventory, TransferFromInventory


# Create your models here.

class InvoiceKeles(models.Model):
    number = models.AutoField(primary_key=True)
    product_to = models.ForeignKey(TransferToInventory, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Invoice #{self.number}"




class InvoiceCreateKeles(models.Model):
    invoice = models.ForeignKey(InvoiceKeles, on_delete=models.CASCADE, related_name='items')
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products_keles')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT,
                             related_name='size_invoice_keles')  # <- related_name qo‘shildi
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_invoice_keles', null=True,
                              blank=True)
    product_to = models.ForeignKey(TransferToInventory, on_delete=models.PROTECT, related_name='transfer_to_keles')
    quantity = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    def __str__(self):
        return str(self.name)  # Make sure CategoryModel has a __str__ method

    class Meta:
        ordering = ['name']
        verbose_name = 'InvoiceModel'
        verbose_name_plural = 'InvoiceModels'


class ProductEntryKeles(models.Model):
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='category_from_keles')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT, related_name='size_from_keles')
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_from_keles')
    product_in = models.ForeignKey(TransferFromInventory, on_delete=models.PROTECT, related_name='transfer_from_keles')
    quantity = models.IntegerField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_in

    class Meta:
        verbose_name = 'ProductEntry'
        verbose_name_plural = 'ProductEntry'


class RemaingInventoryKeles(models.Model):
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='category_remaing_keles')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT, related_name='size_remaing_keles')
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_remaing_keles')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'RemaingModel'
        verbose_name_plural = 'RemaingModel'
