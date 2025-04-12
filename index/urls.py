import imp

from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import Base, Detail, IndexCustom, Categories, Size, ColorAdd, RemaingList, InvoiceCreate, ProductIn, \
    inventory_report, Dashboard

app_name = 'pages'

urlpatterns = [
    path('', IndexCustom, name='cards'),
    path('dashboard/<int:pk>', Dashboard, name='dashboard'),
    path('base/<int:pk>', Base, name='base'),
    path('base/<int:pk>/detail', Detail, name='detail'),
    path('catogory/', Categories, name='category'),
    path('size/', Size, name='size'),
    path('invoice-list/', InvoiceCreate, name='invoice-list'),
    path('color/', login_required(ColorAdd), name='color'),
    path('remaing_list/', RemaingList, name='remaing_list'),
    path('product_in-list/', ProductIn, name='product_in-list'),
    path('turnover/', inventory_report, name='turnover_list'),

]
