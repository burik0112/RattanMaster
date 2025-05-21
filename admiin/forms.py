from PIL.ImageEnhance import Color
from django import forms

from index.models import CategoryModel, SizeModel, ColorModel, RemaingInventoryModel, InvoiceCreateModel, ProductEntry
from keles.models import RemaingInventoryKeles, InvoiceCreateKeles, ProductEntryKeles, InvoiceKeles


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
        model = RemaingInventoryKeles
        fields = ['name', 'size', 'color', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = InvoiceCreateKeles
        fields = ['name', 'size', 'color', 'product_to', 'quantity', 'created_at']


class ProductInCreateForm(forms.ModelForm):
    class Meta:
        model = ProductEntryKeles
        fields = ['name', 'size', 'color', 'product_in', 'quantity', 'created_at']


class RemaingCreateForm(forms.ModelForm):
    class Meta:
        model = RemaingInventoryKeles
        fields = ['name', 'size', 'color', 'quantity']


class RemaingAddKelesForm(forms.ModelForm):
    class Meta:
        model = RemaingInventoryKeles
        fields = ['name', 'size', 'color', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class InvoiceCreateKelesForm(forms.ModelForm):
    class Meta:
        model = InvoiceCreateKeles
        fields = ['name', 'size', 'color', 'product_to', 'quantity', 'created_at']


class ProductInCreateKelesForm(forms.ModelForm):
    class Meta:
        model = ProductEntryKeles
        fields = ['name', 'size', 'color', 'product_in', 'quantity', 'created_at']


class RemaingCreateKelesForm(forms.ModelForm):
    class Meta:
        model = RemaingInventoryKeles
        fields = ['name', 'size', 'color', 'quantity']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class InvoiceKelesForm(forms.ModelForm):
    class Meta:
        model = InvoiceKeles
        fields = ['product_to', 'created_at']


class InvoiceXasanboyForm(forms.ModelForm):
    class Meta:
        model = InvoiceKeles
        fields = ['product_to', 'created_at']