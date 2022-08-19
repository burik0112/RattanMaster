from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from index.models import Category, Model, Product, Responsible, RoomsModel
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CategoryCreateForm, EquipmentCreateForm, ProductUpdateForm, ResponsibleCreateForm, ModelCreateForm, \
    ProductDetailUpdateForm, CategoryEditForm, ModelEditForm, ResponsibleEditForm, RoomsForm
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required


@login_required
def Admin_index(request):
    categories = Category.objects.annotate(count=Count('category'))
    return render(request, 'index.html', {'queryset': categories})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'file/admin-add.html'
    login_url = 'login'
    success_url = reverse_lazy('pages:cards')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResponsibleCreateView(LoginRequiredMixin, CreateView):
    model = Responsible
    form_class = ResponsibleCreateForm
    template_name = 'file/responsible_add.html'
    login_url = 'login'
    success_url = reverse_lazy('pages:responsible')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RoomsCreateView(LoginRequiredMixin, CreateView):
    model = RoomsModel
    form_class = RoomsForm
    template_name = 'file/rooms_add.html'
    login_url = 'login'
    success_url = reverse_lazy('pages:rooms')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ModelCreateView(LoginRequiredMixin, CreateView):
    model = Model
    form_class = ModelCreateForm
    template_name = 'file/model_add.html'
    login_url = 'login'
    success_url = reverse_lazy('pages:models')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def baseview(request, pk):
    query = Product.objects.filter(category_id__id=pk).order_by('pk')
    get_cat = Category.objects.filter(id=pk)
    return render(request, 'admin/admin-base.html', {'query': query, 'get_cat': get_cat})


@login_required
def EquipmentCreateView(request, pk):
    category = Category.objects.get(id=pk)
    form = EquipmentCreateForm()
    if request.method == 'POST':
        form = EquipmentCreateForm(request.POST)
        if form.is_valid():
            # invent = Product.objects.last()
            # try:
            #     inte = int(invent.inventar_number) 
            #     integ = inte + 1
            # except:
            #     integ =  random.randint(1000000000000, 9999999999999999)
            #     uniqe_confirm = Product.objects.filter(inventar_number=integ)
            #     while uniqe_confirm:
            #         integ =  random.randint(1000000000000, 9999999999999999)
            #         if not Product.objects.filter(inventar_number=integ):
            #             break
            # print(type(form.cleaned_data['room_number']))
            equipment = Product(
                category_id=category,
                room_number=form.cleaned_data['room_number'],
                inventar_number=form.cleaned_data['inventar_number'],
                model_id=form.cleaned_data['model_id'],
                responsible_id=form.cleaned_data['responsible_id'],
                seria_number=form.cleaned_data['seria_number'],
                processor=form.cleaned_data['processor'],
                memory=form.cleaned_data['memory'],
                keyword_mouse=form.cleaned_data['keyword_mouse'],
                mac_address=form.cleaned_data['mac_address'],
                ip_address=form.cleaned_data['ip_address'],
                description=form.cleaned_data['description'],
            )
            equipment.save()
            red = equipment.category_id.id
            return redirect('base-view', pk=red)
    return render(request, 'admin/equipment-create.html', {'form': form})


@login_required
def ProductDetailView(request, pk):
    query = Product.objects.filter(id=pk)
    eq = get_object_or_404(Product, pk=pk)
    form = ProductDetailUpdateForm(request.POST or None, instance=eq)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product-detail', pk=eq.pk)
    return render(request, 'admin/admin-detail.html', {'query': query, 'form': form})


@login_required
def ProductUpdateView(request, pk):
    equipment = get_object_or_404(Product, pk=pk)
    red = equipment.category_id.id
    form = ProductUpdateForm(request.POST or None, instance=equipment)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('base-view', pk=red)
    return render(request, 'admin/admin-product-update.html', {'form': form, 'red': red})


@login_required
def ProductDeleteView(request, pk):
    query = Product.objects.get(pk=pk)
    red = query.category_id.id
    if request:
        query.delete()
        return redirect('base-view', pk=red)
    return render(request, 'admin/admin-base.html')


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'admin/admin-search-results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(inventar_number__icontains=query)
        ).order_by('pk')
        return object_list


@login_required
def AdminCategories(request):
    query = Category.objects.all().order_by('pk')
    return render(request, 'file/admin-add.html', {'query': query})


@login_required
def AdminCategoryEdit(request, pk):
    query = get_object_or_404(Category, pk=pk)
    form = CategoryEditForm(request.POST or None, request.FILES or None, instance=query)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin-categories')
    return render(request, 'file/admin-add.html', {'form': form})


@login_required
def AdminCategoryDelete(request, pk):
    query = Category.objects.get(pk=pk)
    if request:
        query.delete()
        return redirect('admin-categories')
    return render(request, 'file/admin-add.html')


@login_required
def AdminModels(request):
    query = Model.objects.all().order_by('pk')
    return render(request, 'file/model_add.html', {'query': query})


@login_required
def AdminModelEdit(request, pk):
    query = get_object_or_404(Model, pk=pk)
    form = ModelEditForm(request.POST or None, request.FILES or None, instance=query)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin-models')
    return render(request, 'admin/model-edit.html', {'form': form})


@login_required
def AdminModelDelete(request, pk):
    query = Model.objects.get(pk=pk)
    if request:
        query.delete()
        return redirect('admin-models')
    return render(request, 'admin/admin-models.html')


@login_required
def AdminResponsibles(request):
    query = Responsible.objects.order_by('pk')
    return render(request, 'file/responsible_add.html', {'query': query})


@login_required
def AdminResponsibleEdit(request, pk):
    query = get_object_or_404(Responsible, pk=pk)
    form = ResponsibleEditForm(request.POST or None, instance=query)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin-responsibles')
    return render(request, 'admin/responsible-edit.html', {'form': form})


@login_required
def AdminResponsibleDelete(request, pk):
    query = Responsible.objects.get(pk=pk)
    if request:
        query.delete()
        return redirect('admin-responsibles')
    return render(request, 'admin/responsibles.html')


def AdminRooms(request):
    queryset = Product.objects.all().order_by('room_number')
    room_list = []
    for u in queryset:
        if u.room_number not in room_list:
            room_list.append(u.room_number)
    return render(request, 'file/rooms_add.html', {'queryset': queryset, 'room_list': room_list})


def AdminRoomDetail(request, pk):
    query = Product.objects.filter(room_number=str(pk)).order_by('pk')
    qr_list = []
    for q in query:
        Jihoz = {
            f"Jihoz id: {q.pk}, Inventar raqami: {q.inventar_number}, Modeli: {q.model_id.name}, Javobgar shaxs: {q.responsible_id.fullname}, Xona: {q.room_number}"}
        qr_list.append(Jihoz)
    return render(request, 'file/rooms_add.html', {'query': query, "qr_list": qr_list})
