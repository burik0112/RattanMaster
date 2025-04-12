from itertools import count

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from .models import CategoryModel, ColorModel, SizeModel, InvoiceCreateModel, RemaingInventoryModel, ProductEntry, \
    TransferToInventory
from django.db.models import Count, Sum


def IndexCustom(request):
    total_quantity = InvoiceCreateModel.objects.aggregate(Sum('quantity'))['quantity__sum']
    total_product_in = ProductEntry.objects.aggregate(Sum('quantity'))['quantity__sum']
    total_remaing = RemaingInventoryModel.objects.aggregate(Sum('quantity'))['quantity__sum']
    # Если нет данных, установим значение в 0
    if total_quantity is None:
        total_quantity = 0

    if total_product_in is None:
        total_product_in = 0

    if total_remaing is None:
        total_product_in = 0

    # Аннотируем категории, добавляя количество продуктов в каждой категории
    categories_with_product_count = CategoryModel.objects.annotate(
        count=Count('products')
    )
    transfer_to = TransferToInventory.objects.annotate(
        count=Count('transfer_to')
    )

    # Возвращаем результат в шаблон
    return render(request, 'catalog_category.html', {
        'query': categories_with_product_count,
        'total_quantity': total_quantity,
        'total_product_in': total_product_in,
        'total_remaing': total_remaing,
        'transfer_to': transfer_to
    })


def Base(request, pk):
    query = InvoiceCreateModel.objects.filter(name__id=pk)
    return render(request, 'index.html', {'query': query})


def Detail(request, pk):
    query = InvoiceCreateModel.objects.filter(pk=pk)
    return render(request, 'detail.html', {'query': query})


def Categories(request):
    query = CategoryModel.objects.all()
    return render(request, 'category-cat.html', {'query': query})


def ColorAdd(request):
    query = ColorModel.objects.all()
    return render(request, 'color.html', {'query': query})


def Size(request):
    query = SizeModel.objects.all()  # Now this refers to the model
    return render(request, 'size-catalog.html', {'query': query})


def InvoiceCreate(request):
    invoice = InvoiceCreateModel.objects.all()  # Now this refers to the model
    return render(request, 'invoice-catalog.html', {'invoice': invoice})


def ProductIn(request):
    product_in = ProductEntry.objects.all()  # Now this refers to the model
    return render(request, 'product_in-catalog.html', {'product_in': product_in})


def RemaingList(request):
    remaing = RemaingInventoryModel.objects.all()
    return render(request, 'remaing-list.html', {'remaing': remaing})


def inventory_report(request):
    inventory_data = []

    # 1. Sobiraem vse unikal'nye kombinatsii iz vseh 3 modeley
    entry_keys = ProductEntry.objects.values_list('name', 'size', 'color').distinct()
    remaining_keys = RemaingInventoryModel.objects.values_list('name', 'size', 'color').distinct()
    invoice_keys = InvoiceCreateModel.objects.values_list('name', 'size', 'color').distinct()

    # 2. Ob'edinyaem vse kombinatsii v odin set
    combined_keys = set(entry_keys) | set(remaining_keys) | set(invoice_keys)

    # 3. Prohodim po vsem kombinatsiyam
    for name_id, size_id, color_id in combined_keys:
        # Schitaem ob'emy iz vseh modeley
        total_in = ProductEntry.objects.filter(name_id=name_id, size_id=size_id, color_id=color_id) \
                       .aggregate(total=Sum('quantity'))['total'] or 0

        total_remaining = RemaingInventoryModel.objects.filter(name_id=name_id, size_id=size_id, color_id=color_id) \
                              .aggregate(total=Sum('quantity'))['total'] or 0

        total_invoice = InvoiceCreateModel.objects.filter(name_id=name_id, size_id=size_id, color_id=color_id) \
                            .aggregate(total=Sum('quantity'))['total'] or 0

        # Poluchaem lyuboy ob'ekt dlya dostupa k title
        obj = (ProductEntry.objects.select_related('name', 'size', 'color')
               .filter(name_id=name_id, size_id=size_id, color_id=color_id).first()
               or
               RemaingInventoryModel.objects.select_related('name', 'size', 'color')
               .filter(name_id=name_id, size_id=size_id, color_id=color_id).first()
               or
               InvoiceCreateModel.objects.select_related('name', 'size', 'color')
               .filter(name_id=name_id, size_id=size_id, color_id=color_id).first())

        if obj:
            inventory_data.append({
                'category_id': obj.name.id,
                'category_title': obj.name.title,
                'size_title': obj.size.title,
                'color_title': obj.color.title,
                'total_in': total_in,
                'total_remaining': total_remaining,
                'total_invoice': total_invoice,
                'remaining_stock': total_in + total_remaining - total_invoice
            })

    return render(request, 'turnover.html', {'inventory_data': inventory_data})


def Dashboard(request, pk):
    query = InvoiceCreateModel.objects.filter(product_to__id=pk)
    return render(request, 'dashboard.html', {'query': query})
