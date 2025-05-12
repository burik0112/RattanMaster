from django.contrib import admin

from admiin.models import CustomUser


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['role']