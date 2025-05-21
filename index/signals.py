from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver

from index.models import InvoiceCreateModel, TransferFromInventory
from keles.models import ProductEntryKeles


@receiver(post_save, sender=InvoiceCreateModel)
def create_product_entry_keles(sender, instance, created, **kwargs):
    if created and instance.invoice.product_to.title == "Склад Келес":
        try:
            hasanboy_from = TransferFromInventory.objects.get(title="Склад Хасанбой")
            ProductEntryKeles.objects.create(
                name=instance.name,
                size=instance.size,
                color=instance.color,
                quantity=instance.quantity,
                product_in=hasanboy_from,
                created_at=instance.created_at
            )
        except TransferFromInventory.DoesNotExist:
            # В лог или просто проигнорировать
            print("Склад Хасанов не найден. Запись не создана.")
