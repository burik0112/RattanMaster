import uuid

from django.db import models
from django.utils import timezone


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'CategoryModel'
        verbose_name_plural = 'CategoryModel'


class SizeModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class TransferFromInventory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        print(f"type of title: {type(self.title)}")
        return self.title

    class Meta:
        verbose_name = 'TransferFromInventory'
        verbose_name_plural = 'TransferFromInventory'


class TransferToInventory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TransferToInventory'
        verbose_name_plural = 'TransferToInventory'


class ColorModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ColorModel'
        verbose_name_plural = 'ColorsModel'

class Invoice(models.Model):
    number = models.AutoField(primary_key=True)
    product_to = models.ForeignKey(TransferToInventory, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Invoice #{self.number}"


class InvoiceCreateModel(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT)
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_invoice', null=True, blank=True)
    quantity = models.IntegerField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.name)  # Make sure CategoryModel has a __str__ method

    class Meta:
        ordering = ['name']
        verbose_name = 'InvoiceModel'
        verbose_name_plural = 'InvoiceModels'


class ProductEntry(models.Model):
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='category_from')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT, related_name='size_from')
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_from')
    product_in = models.ForeignKey(TransferFromInventory, on_delete=models.PROTECT, related_name='transfer_from')
    quantity = models.IntegerField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_in

    class Meta:
        verbose_name = 'ProductEntry'
        verbose_name_plural = 'ProductEntry'


class RemaingInventoryModel(models.Model):
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='category_remaing')
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT, related_name='size_remaing')
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='color_remaing')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name.title} - {self.size.title} - {self.color.title} ({self.quantity})"

    class Meta:
        verbose_name = 'RemaingModel'
        verbose_name_plural = 'RemaingModel'




class ProductPriceModel(models.Model):
    name = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    size = models.ForeignKey(SizeModel, on_delete=models.PROTECT)
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} | {self.size} | {self.color} - {self.price}"



