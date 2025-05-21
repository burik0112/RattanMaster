from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Начальник', 'Начальник'),
        ('Менеджер склада', 'Менеджер склада'),
        ('Менеджер склада Келес', 'Менеджер склада Келес'),
        ('Оператор склада', 'Оператор склада'),
        ('Оператор склада Келес', 'Оператор склада Келес'),
        ('Сотрудник приемки', 'Сотрудник приемки'),
        ('Сотрудник приемки Келес', 'Сотрудник приемки Келес'),
        ('Наблюдатель', 'Наблюдатель'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    img = models.ImageField(upload_to='media/user', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'UserModel'
        verbose_name_plural = 'UserModel'
