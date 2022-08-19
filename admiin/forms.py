from django import forms
from index.models import Category, Model, Product, Responsible, RoomsModel
from django.core.exceptions import ValidationError


class RoomsForm(forms.ModelForm):
    class Meta:
        model = RoomsModel
        fields = '__all__'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
        labels = {
            'name': 'Kategoriya nomi ',
            'image': 'Kategoriya rasmi ',
        }


class ResponsibleCreateForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ['fullname', 'description']
        labels = {
            'fullname': 'Javobgar shaxs ism-familiyasi ',
            'description': 'Shaxs haqida izoh ',
        }


class ModelCreateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'Jihoz modeli nomi ',
            'image': 'Jihoz modeli rasmi ',
            'description': 'Izoh ',
        }
        print(labels)


mouse_choices = (
    ('simli', 'simli'),
    ('simsiz', 'simsiz'),
)
status_choices = (
    ('Ishlatilmoqda', 'Ishlatilmoqda'),
    ('Olib ketilgan', 'Olib ketilgan'),
    ('Yaroqsiz', 'Yaroqsiz'),
    ('Zahirada', 'Zahirada'),
)


class EquipmentCreateForm(forms.Form):
    room_number = forms.ChoiceField(choices=((str(x), x) for x in range(150, 540)), label='Xona raqami',
                                    widget=forms.Select(attrs={'class': "form-control"}))
    inventar_number = forms.IntegerField(required=True, label='Inventar raqami',
                                         widget=forms.NumberInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.all(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    processor = forms.CharField(max_length=70, label='Protsessori', required=False,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    memory = forms.CharField(max_length=70, label='Xotira hajmi', required=False,
                             widget=forms.TextInput(attrs={'class': "form-control"}))
    keyword_mouse = forms.ChoiceField(choices=mouse_choices, label='Klaviatura va sichqoncha turi',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    mac_address = forms.CharField(max_length=50, label='MAC Addressi', required=False,
                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    ip_address = forms.CharField(max_length=50, label='IP Addressi', required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    def clean_inventar_number(self):
        inventar_number = self.cleaned_data['inventar_number']
        qs = Product.objects.filter(inventar_number=inventar_number)
        if qs:
            raise ValidationError('Bu inventar raqam boshqa jihozga berilgan')
        return inventar_number


class ProductUpdateForm(forms.ModelForm):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), label='Kategoriyasi',
                                         widget=forms.Select(attrs={'class': "form-control"}))
    room_number = forms.ChoiceField(choices=((str(x), x) for x in range(150, 540)), label='Xona raqami',
                                    widget=forms.Select(attrs={'class': "form-control"}))
    inventar_number = forms.IntegerField(label='Inventar raqami',
                                         widget=forms.NumberInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.all(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    processor = forms.CharField(max_length=70, label='Protsessori', required=False,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    memory = forms.CharField(max_length=70, label='Xotira hajmi', required=False,
                             widget=forms.TextInput(attrs={'class': "form-control"}))
    keyword_mouse = forms.ChoiceField(choices=mouse_choices, label='Klaviatura va sichqoncha turi',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    mac_address = forms.CharField(max_length=50, label='MAC Addressi', required=False,
                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    ip_address = forms.CharField(max_length=50, label='IP Addressi', required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))
    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        model = Product
        exclude = ('qr_code',)


class ProductDetailUpdateForm(forms.ModelForm):
    status_choices = (
        ('Ishlatilmoqda', 'Ishlatilmoqda'),
        ('Olib Ketilgan', 'Olib Ketilgan'),
        ('Yaroqsiz', 'Yaroqsiz'),
        ('Zahirada', 'Zahirada'),
    )

    status = forms.ChoiceField(choices=status_choices, label='', widget=forms.Select(attrs={'class': "form-control"}))
    responsible_person = forms.CharField(max_length=256, required=False, label='Masul shaxs',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = Product
        fields = ['status', 'responsible_person']


class CategoryEditForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))

    class Meta:
        model = Category
        fields = ['name', 'image']


class ModelEditForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Model
        fields = ['name', 'image', 'description']


class ResponsibleEditForm(forms.ModelForm):
    fullname = forms.CharField(max_length=70, label='Ism-familiya', required=True,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Izoh', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Responsible
        fields = ['fullname', 'description']
