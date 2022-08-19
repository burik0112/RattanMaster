from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils.translation import gettext_lazy as _


class RoomsModel(models.Model):
    rooms = models.CharField(max_length=10, verbose_name=_('rooms'))
    floor = models.CharField(max_length=10, verbose_name=_('floor'))

    def __str__(self):
        return self.rooms

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'))

    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'))

    def __str__(self) -> str:
        return self.name


class Responsible(models.Model):
    fullname = models.CharField(max_length=100, verbose_name=_('fullname'))
    description = models.TextField(verbose_name=_('description'))

    def __str__(self) -> str:
        return self.fullname


class Product(models.Model):
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, blank=True, verbose_name=_('category_id'))
    room_number = models.CharField(max_length=4, verbose_name=_('room_number'))
    inventar_number = models.IntegerField(unique=True, blank=True, verbose_name=_('inventar_number'))
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, verbose_name=_('model_id'))
    responsible_id = models.ForeignKey(Responsible, on_delete=models.CASCADE, verbose_name=_('responsible_id'))
    seria_number = models.CharField(max_length=70, blank=True, null=True, verbose_name=_('seria_number'))
    processor = models.CharField(max_length=70, blank=True, verbose_name=_('processor'))
    memory = models.CharField(max_length=70, blank=True, verbose_name=_('memory'))
    keyword_mouse = models.CharField(max_length=6, blank=True, verbose_name=_('keyword_mouse'))
    mac_address = models.CharField(max_length=50, blank=True, verbose_name=_('mac_address'))
    ip_address = models.CharField(max_length=50, blank=True, verbose_name=_('ip_address'))
    description = models.TextField(verbose_name=_('description'))
    images = models.ImageField(upload_to='person', verbose_name=_('images'))
    status = models.CharField(max_length=40, null=True, default='Ishlatilmoqda', verbose_name=_('status'))
    qr_code = models.ImageField(blank=True, upload_to='images/code', verbose_name=_('qr_code'))
    responsible_person = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('responsible_person'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('updated_at'))

    def __str__(self) -> str:
        return str(self.inventar_number)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(
            f'Inventar raqami: {self.inventar_number}\n Modeli: {self.model_id.name} \n Javobgar shaxs: {self.responsible_id.fullname}\n Seria raqami: {self.seria_number} \n Xona: {self.room_number} \n MAC Address: {self.mac_address}\n Masul Shaxs: {self.responsible_person}\n ')
        qr_offset = Image.new('RGB', (570, 570), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.inventar_number}--{self.responsible_id.fullname}--qrcode.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
