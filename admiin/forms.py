from PIL.ImageEnhance import Color
from django import forms

from index.models import CategoryModel, SizeModel, ColorModel, RemaingInventoryModel, InvoiceCreateModel, ProductEntry


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title']



class SizeForm(forms.ModelForm):
    class Meta:
        model = SizeModel
        fields = ['title']



class ColorForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = ['title']



class RemaingAddForm(forms.ModelForm):
    class Meta:
        model = RemaingInventoryModel
        fields = ['name', 'size', 'color', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = InvoiceCreateModel
        fields = ['name', 'size', 'color', 'product_to', 'quantity', 'created_at']


class ProductInCreateForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = ['name', 'size', 'color', 'product_in', 'quantity', 'created_at']



class RemaingCreateForm(forms.ModelForm):
    class Meta:
        model = RemaingInventoryModel
        fields = ['name', 'size', 'color', 'quantity']


