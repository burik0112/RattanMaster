import imp

from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import Base, Detail, IndexCustom, Categories, Size, ColorAdd, RemaingList, InvoiceCreate, ProductIn, \
    inventory_report, Dashboard, combined_inventory, shop_summary, shop_list, shop_export_excel, \
    login_view, logout_view, logout_success_view, invoice_list, invoice_detail, export_to_excel

app_name = 'pages'

urlpatterns = [
    path('dashboar2/', IndexCustom, name='cards'),
    path('logout/', logout_view, name='logout'),
    path('logout-success/', logout_success_view, name='logout-success'),
    path('', login_view, name='login'),
    path('dashboard/<int:pk>', login_required(Dashboard), name='dashboard'),
    path('base/<int:pk>', login_required(Base), name='base'),
    path('base/<int:pk>/detail', login_required(Detail), name='detail'),
    path('catogory/', login_required(Categories), name='category'),
    path('size/', login_required(Size), name='size'),
    path('invoice-list/', login_required(InvoiceCreate), name='invoice-list2'),
    path('color/', login_required(ColorAdd), name='color'),
    path('remaing_list/', login_required(RemaingList), name='remaing_list'),
    path('product_in-list/', login_required(ProductIn), name='product_in-list'),
    path('turnover/', inventory_report, name='turnover_list'),
    path('total-turnover/', combined_inventory, name='total-turnover_list'),
    path('transfer_to/', shop_list, name='transfer-to'),
    path('shop_report/<int:pk>/', shop_summary, name='shop-report'),
    path('shop/<int:pk>/export-excel/', shop_export_excel, name='shop-export-excel'),
    path('invoices/', invoice_list, name='invoice-list'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('invoice/<int:invoice_id>/export/', export_to_excel, name='export-invoice'),
]
