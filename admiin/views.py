import openpyxl
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.formats import date_format
from openpyxl.styles import Alignment, Font, Border, Side
from openpyxl.utils import get_column_letter
from reportlab.pdfgen import canvas
from admiin.forms import CategoryForm, SizeForm, ColorForm, InvoiceCreateForm, ProductInCreateForm, RemaingCreateForm
from index.models import CategoryModel, SizeModel, ColorModel, RemaingInventoryModel, InvoiceCreateModel, \
    TransferToInventory, TransferFromInventory, ProductEntry


def AdminCategoryEdit(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('pages:category')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'edit/category-edit.html', {'form': form})


def CategoryDelete(request, pk):
    query = get_object_or_404(CategoryModel, pk=pk)
    if request:
        query.delete()
        return redirect('pages:category')  # Change to your actual URL name
    return render(request, 'category-cat.html')


def AdminSizeEdit(request, pk):
    size = get_object_or_404(SizeModel, pk=pk)

    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            return redirect('pages:size')
    else:
        form = SizeForm(instance=size)

    return render(request, 'edit/size-edit.html', {'form': form})


def SizeDelete(request, pk):
    query = get_object_or_404(SizeModel, pk=pk)
    if request:
        query.delete()
        return redirect('pages:size')  # Change to your actual URL name
    return render(request, 'size-catalog.html')


def Color_create_or_edit(request, pk=None):
    if pk:  # If pk is passed, it's an edit operation
        color = get_object_or_404(ColorModel, pk=pk)
    else:  # No pk, create new category
        color = None

    # Initialize form with existing category data (for editing)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)  # Bind form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pages:color')  # Redirect to a list page after saving
    else:
        form = ColorForm(instance=color)  # Bind form with category data (for editing or new)

    return render(request, 'file/color-add.html', {'form': form})


def ColorDelete(request, pk):
    query = get_object_or_404(ColorModel, pk=pk)
    if request:
        query.delete()
        return redirect('pages:color')  # Change to your actual URL name
    return render(request, 'size-catalog.html')


def Category_create_or_edit(request, pk=None):
    if pk:  # If pk is passed, it's an edit operation
        cat = get_object_or_404(CategoryModel, pk=pk)
    else:  # No pk, create new category
        cat = None

    # Initialize form with existing category data (for editing)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cat)  # Bind form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pages:category')  # Redirect to a list page after saving
    else:
        form = CategoryForm(instance=cat)  # Bind form with category data (for editing or new)

    return render(request, 'file/category-add.html', {'form': form})


def Size_create_or_edit(request, pk=None):
    if pk:  # If pk is passed, it's an edit operation
        size = get_object_or_404(SizeModel, pk=pk)
    else:  # No pk, create new category
        size = None

    # Initialize form with existing category data (for editing)
    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)  # Bind form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pages:size')  # Redirect to a list page after saving
    else:
        form = SizeForm(instance=size)  # Bind form with category data (for editing or new)

    return render(request, 'file/size-add.html', {'form': form})


def AddRemaing(request):
    if request.method == 'POST':
        name_id = request.POST.get('name')
        size_id = request.POST.get('size')
        color_id = request.POST.get('color')
        quantity = request.POST.get('quantity')

        # Get actual related model instances
        name = CategoryModel.objects.get(id=name_id)
        size = SizeModel.objects.get(id=size_id)
        color = ColorModel.objects.get(id=color_id)

        # Save to database
        RemaingInventoryModel.objects.create(
            name=name,
            size=size,
            color=color,
            quantity=quantity
        )

        return redirect('pages:remaing_list')  # change this to your actual url name

    # For GET: show the form and pass dropdown data
    categories = CategoryModel.objects.all()
    sizes = SizeModel.objects.all()
    colors = ColorModel.objects.all()

    return render(request, 'file/remaing-add.html', {
        'categories': categories,
        'sizes': sizes,
        'colors': colors,
    })


def InvoiceCreate(request):
    if request.method == 'POST':
        name_ids = request.POST.getlist('name')
        size_ids = request.POST.getlist('size')
        color_ids = request.POST.getlist('color')
        product_to_ids = request.POST.getlist('product_to')
        quantities = request.POST.getlist('quantity')

        created_at = timezone.now().date()
        created_ids = []  # Список ID для экспорта

        for name_id, size_id, color_id, product_to_id, quantity in zip(name_ids, size_ids, color_ids, product_to_ids,
                                                                       quantities):
            name = CategoryModel.objects.get(id=name_id)
            size = SizeModel.objects.get(id=size_id)
            color = ColorModel.objects.get(id=color_id)
            product_to = TransferToInventory.objects.get(id=product_to_id)

            invoice = InvoiceCreateModel.objects.create(
                name=name,
                size=size,
                color=color,
                product_to=product_to,
                quantity=quantity,
                created_at=created_at
            )
            created_ids.append(invoice.id)  # Запоминаем ID созданной записи

        # Сохраняем ID в сессию пользователя
        request.session['last_invoice_ids'] = created_ids

        # Можно редиректить сразу на экспорт
        return redirect('add:export_to_excel')  # Или на страницу, где кнопка "Скачать Excel"

    context = {
        'categories': CategoryModel.objects.all(),
        'sizes': SizeModel.objects.all(),
        'colors': ColorModel.objects.all(),
        'transfer_to': TransferToInventory.objects.all()
    }
    return render(request, 'file/product_add.html', context)


def EntryCreate(request):
    if request.method == 'POST':
        name_id = request.POST.get('name')
        size_id = request.POST.get('size')
        color_id = request.POST.get('color')
        product_in_id = request.POST.get('product_in')
        quantity = request.POST.get('quantity')

        # Get actual related model instances
        name = CategoryModel.objects.get(id=name_id)
        size = SizeModel.objects.get(id=size_id)
        color = ColorModel.objects.get(id=color_id)
        product_in = TransferFromInventory.objects.get(id=product_in_id)

        # Manually set created_at to current date
        created_at = timezone.now().date()

        # Save to database
        ProductEntry.objects.create(
            name=name,
            size=size,
            color=color,
            product_in=product_in,
            quantity=quantity,
            created_at=created_at
        )

        return redirect('pages:product_in-list')  # Change this to your actual URL name

    # For GET request: Show the form and pass dropdown data
    categories = CategoryModel.objects.all()
    sizes = SizeModel.objects.all()
    colors = ColorModel.objects.all()
    product_in = TransferFromInventory.objects.all()

    return render(request, 'file/product-in.html', {
        'categories': categories,
        'sizes': sizes,
        'colors': colors,
        'product_in': product_in,
    })


def InvoiceEdit(request, pk):
    obj = get_object_or_404(InvoiceCreateModel, pk=pk)
    if request.method == 'POST':
        form = InvoiceCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pages:invoice-list')  # replace with your actual detail or success view
    else:
        form = InvoiceCreateForm(instance=obj)
    return render(request, 'edit/invoice-edit.html', {'form': form})


def InvoiceDelete(request, pk):
    query = get_object_or_404(InvoiceCreateModel, pk=pk)
    if request:
        query.delete()
        return redirect('pages:invoice-list')  # Change to your actual URL name
    return render(request, 'invoice-catalog.html')


def ProductInEdit(request, pk):
    obj = get_object_or_404(ProductEntry, pk=pk)
    if request.method == 'POST':
        form = ProductInCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pages:product_in-list')  # replace with your actual detail or success view
    else:
        form = ProductInCreateForm(instance=obj)
    return render(request, 'edit/product-in-edit.html', {'form': form})


def ProductInDelete(request, pk):
    query = get_object_or_404(ProductEntry, pk=pk)
    if request:
        query.delete()
        return redirect('pages:product_in-list')  # Change to your actual URL name
    return render(request, 'product_in-catalog.html')


def RemaingEdit(request, pk):
    obj = get_object_or_404(RemaingInventoryModel, pk=pk)
    if request.method == 'POST':
        form = RemaingCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pages:remaing_list')  # replace with your actual detail or success view
    else:
        form = RemaingCreateForm(instance=obj)
    return render(request, 'edit/remaing-edit.html', {'form': form})


def RemaingDelete(request, pk):
    query = get_object_or_404(RemaingInventoryModel, pk=pk)
    if request:
        query.delete()
        return redirect('pages:remaing_list')  # Change to your actual URL name
    return render(request, 'remaing-list.html')


def export_to_excel(request):
    ids = request.session.get('last_invoice_ids', [])
    if not ids:
        return HttpResponse("Нет данных для экспорта.")

    items = InvoiceCreateModel.objects.filter(id__in=ids)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Накладная"

    # Стили
    bold_font = Font(bold=True)
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    # Заголовок
    invoice = items.first()
    invoice_date = date_format(invoice.created_at, 'd.m.Y')

    ws.merge_cells('A1:F1')
    ws['A1'] = f"НАКЛАДНАЯ № {invoice.id}"
    ws['A1'].font = Font(size=14, bold=True)
    ws['A1'].alignment = center

    ws.merge_cells('A2:F2')
    ws['A2'] = f'от "{invoice_date}"'
    ws['A2'].alignment = Alignment(horizontal="right")

    ws['A4'] = "От кого:"
    ws['A5'] = f"Кому:"
    ws['B4'] = "OOO RATTAN MASTER"
    ws['B5'] = f"{invoice.product_to or ''}"
    # Таблица
    headers = ["№ п/п", "Наименование", "Размер", "Цвет", "Ед. изм.", "Количество"]
    ws.append([])
    ws.append(headers)

    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=7, column=col_num)
        cell.value = header
        cell.font = bold_font
        cell.alignment = center
        cell.border = border
        ws.column_dimensions[get_column_letter(col_num)].width = 20 if col_num != 1 else 8

    # Данные
    row = 8
    for index, item in enumerate(items, start=1):
        values = [
            index,
            item.name.title,
            item.size.title if item.size else '',
            item.color.title if item.color else '',
            "шт",
            item.quantity
        ]
        for col, val in enumerate(values, 1):
            cell = ws.cell(row=row, column=col, value=val)
            cell.alignment = center
            cell.border = border
        row += 1

    # Подписи
    row += 2
    ws.merge_cells(f'A{row}:C{row}')
    ws[f'A{row}'] = "Сдал: ________________   Ф. И. О."
    ws.merge_cells(f'D{row}:F{row}')
    ws[f'D{row}'] = "Принял: ________________   Ф. И. О."

    # Ответ клиенту
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="nakladnaya.xlsx"'
    wb.save(response)
    return response


def export_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)

    y = 800
    p.drawString(100, y, 'Invoice List')
    y -= 30

    items = InvoiceCreateModel.objects.all()
    for item in items:
        p.drawString(100, y,
                     f"{item.name.title} | {item.size.title} | {item.color.title} | {item.product_to.title} | {item.quantity}")
        y -= 20

    p.showPage()
    p.save()
    return response
