from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Model, Responsible, Product, RoomsModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'name', 'image']


@admin.register(Model)
class ModelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']


@admin.register(Responsible)
class ResponsibleModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'fullname', 'description']


@admin.register(Product)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'category_id', 'room_number', 'inventar_number', 'model_id', 'responsible_id', 'seria_number',
                    'processor', 'memory', 'keyword_mouse', 'mac_address', 'ip_address', 'description', 'images',
                    'status', 'qr_code', 'responsible_person', 'created_at', 'updated_at']


@admin.register(RoomsModel)
class RoomsModelAdmin(admin.ModelAdmin):
    list_display = ['rooms', 'floor']

