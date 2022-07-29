from django.contrib import admin
from .models import Category, Model, Responsible, Product

admin.site.register(Category)
admin.site.register(Model)
admin.site.register(Responsible)
admin.site.register(Product)
