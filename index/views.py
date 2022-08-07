from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product, Model, Responsible
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def Index(request):
    # query = Category.objects.annotate(count=Count('category'))
    # return render(request, 'registration/login.html')
    return render(request, 'index.html')


def IndexCustom(request):
    query = Category.objects.annotate(count=Count('category'))
    return render(request, 'pages-directory.html', {'query': query})


def Base(request, pk):
    query = Product.objects.filter(category_id__id=pk)
    return render(request, 'base.html', {'query': query})


def Detail(request, pk):
    query = Product.objects.filter(pk=pk)
    return render(request, 'detail.html', {'query': query})


def Categories(request):
    query = Category.objects.all()
    return render(request, 'categories.html', {'query': query})


def DeviceModels(request):
    query = Model.objects.all()
    return render(request, 'models.html', {'query': query})


def ResponsiblePeople(request):
    query = Responsible.objects.all()
    return render(request, 'responsible.html', {'query': query})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(inventar_number__icontains=query)
        )
        return object_list
