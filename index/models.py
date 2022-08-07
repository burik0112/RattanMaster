from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')

    def __str__(self) -> str:
        return self.name

    
class Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images')

    def __str__(self) -> str:
        return self.name

class Responsible(models.Model):
    fullname = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.fullname

class Product(models.Model):
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, blank=True)
    room_number = models.CharField(max_length=4)
    inventar_number = models.IntegerField(unique=True, blank=True)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True)
    responsible_id = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    seria_number = models.CharField(max_length=70, blank=True, null=True)
    processor = models.CharField(max_length=70, blank=True)
    memory = models.CharField(max_length=70, blank=True)
    keyword_mouse = models.CharField(max_length=6, blank=True)
    mac_address = models.CharField(max_length=50, blank=True)
    ip_address = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    images = models.ImageField(upload_to='person')
    status = models.CharField(max_length=40, null=True, default='Ishlatilmoqda')
    qr_code = models.ImageField(blank=True, upload_to='images/code')
    responsible_person = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.inventar_number)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f'Inventar raqami: {self.inventar_number}\n Modeli: {self.model_id.name} \n Javobgar shaxs: {self.responsible_id.fullname}\n Seria raqami: {self.seria_number} \n Xona: {self.room_number} \n MAC Address: {self.mac_address}\n Masul Shaxs: {self.responsible_person}\n ')
        qr_offset = Image.new('RGB', (570, 570), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.inventar_number}--{self.responsible_id.fullname}--qrcode.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
