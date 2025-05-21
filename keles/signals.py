from django.db.models.signals import post_save
from django.dispatch import receiver

from index.models import TransferFromInventory, ProductEntry
from keles.models import InvoiceCreateKeles


@receiver(post_save, sender=InvoiceCreateKeles)
def create_product_entry_hasanboy(sender, instance, created, **kwargs):
    if created and instance.invoice.product_to.title == "Склад Хасанбой":
        try:
            hasanboy_from = TransferFromInventory.objects.get(title="Склад Келес")  # откуда прибыло
            ProductEntry.objects.create(
                name=instance.name,
                size=instance.size,
                color=instance.color,
                quantity=instance.quantity,
                product_in=hasanboy_from,  # вход — из Келеса
                created_at=instance.created_at
            )
        except TransferFromInventory.DoesNotExist:
            print("Склад Келес не найден. Запись не создана.")