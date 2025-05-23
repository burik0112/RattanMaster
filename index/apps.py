from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvoiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
    verbose_name = _('Index')

    def ready(self):
        import index.signals