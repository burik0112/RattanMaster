from django.contrib.auth.decorators import login_required
from django.urls import path

from index.urls import app_name
from keles.views import Base, Detail, InvoiceCreateFromKeles, RemaingListKeles, ProductInKeles, TurnoverKeles, \
    Dashboard, Client_ReportKeles, invoice_list, invoice_detail, export_to_excel

app_name = 'keles'

urlpatterns = [
    path('keles_dashboard', Dashboard, name='dashboard_keles'),
    path('client_report/<int:pk>', login_required(Client_ReportKeles), name='dashboard'),
    path('base/<int:pk>', login_required(Base), name='base'),
    path('base/<int:pk>/detail', login_required(Detail), name='detail'),
    path('invoice-list/', login_required(InvoiceCreateFromKeles), name='invoice-list'),
    path('remaing_list/', login_required(RemaingListKeles), name='remaing_list'),
    path('product_in-list/', login_required(ProductInKeles), name='product_in-list'),
    path('turnover/', TurnoverKeles, name='turnover_list'),
    path('invoices/', invoice_list, name='invoice-list-keles'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice-detail-keles'),
    path('invoice/<int:invoice_id>/export/', export_to_excel, name='export-invoice-keles'),
]
