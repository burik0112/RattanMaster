from django.contrib.auth.decorators import login_required
from django.urls import path

from admiin.views import AdminCategoryEdit, AdminSizeEdit, Category_create_or_edit, \
    Color_create_or_edit, Size_create_or_edit, AddRemaing, InvoiceCreate, EntryCreate, InvoiceEdit, InvoiceDelete, \
    ProductInEdit, ProductInDelete, RemaingEdit, RemaingDelete, ColorDelete, SizeDelete, CategoryDelete, \
    export_to_excel, AddRemaingKeles, RemaingEditKeles, RemaingDeleteKeles, InvoiceDeleteKeles, \
    ProductInDeleteKeles, ProductInEditKeles, InvoiceEditKeles, EntryCreateKeles, \
    export_to_excelkeles, InvoiceCreate2Model

app_name = 'add'

urlpatterns = [
    path('category/edit/<int:pk>/', login_required(AdminCategoryEdit), name='category-edit'),
    path('size/edit/<int:pk>/', login_required(AdminSizeEdit), name='size-edit'),
    path('color/create/', login_required(Color_create_or_edit), name='color-create'),
    path('color/edit/<int:pk>/', login_required(Color_create_or_edit), name='color-edit'),
    path('category/create/', login_required(Category_create_or_edit), name='category-create'),
    path('category/edit/<int:pk>/', login_required(Category_create_or_edit), name='category-edit'),
    path('size/create/', login_required(Size_create_or_edit), name='size-create'),
    path('size/edit/<int:pk>/', login_required(Size_create_or_edit), name='size-edit'),  # List all products
    path('remaing-add/', login_required(AddRemaing), name='remaing-add'),
    path('invoice-create/', login_required(InvoiceCreate), name='invoice-create'),
    path('product-in/', login_required(EntryCreate), name='product-in'),
    path('product-in-edit/<int:pk>/', login_required(ProductInEdit), name='product-in-edit'),
    path('product-in-delete/<int:pk>/', login_required(ProductInDelete), name='product-in-delete'),
    path('invoice-edit/<int:pk>/', login_required(InvoiceEdit), name='invoice-edit'),
    path('invoice-delete/<int:pk>/', login_required(InvoiceDelete), name='invoice-delete'),
    path('remaing-edit/<int:pk>/', login_required(RemaingEdit), name='remaing-edit'),
    path('remaing-delete/<int:pk>/', login_required(RemaingDelete), name='remaing-delete'),
    path('category-delete/<int:pk>/', login_required(CategoryDelete), name='category-delete'),
    path('size-delete/<int:pk>/', login_required(SizeDelete), name='size-delete'),
    path('color-delete/<int:pk>/', login_required(ColorDelete), name='color-delete'),
    path('export-excel/', export_to_excel, name='export_to_excel'),
    path('keles/remaing-add/', login_required(AddRemaingKeles), name='remaing-add-keles'),
    path('keles/invoice-create/', login_required(InvoiceCreate2Model), name='invoice-create-keles'),
    path('keles/product-in/', login_required(EntryCreateKeles), name='product-in-keles'),
    path('keles/product-in-edit/<int:pk>/', login_required(ProductInEditKeles), name='product-in-edit-keles'),
    path('keles/product-in-delete/<int:pk>/', login_required(ProductInDeleteKeles), name='product-in-delete-keles'),
    path('keles/invoice-edit/<int:pk>/', login_required(InvoiceEditKeles), name='invoice-edit-keles'),
    path('keles/invoice-delete/<int:pk>/', login_required(InvoiceDeleteKeles), name='invoice-delete-keles'),
    path('keles/remaing-edit/<int:pk>/', login_required(RemaingEditKeles), name='remaing-edit-keles'),
    path('keles/remaing-delete/<int:pk>/', login_required(RemaingDeleteKeles), name='remaing-delete-keles'),
    path('keles/export-excel/', login_required(export_to_excelkeles), name='export_to_excel_keles'),
]
