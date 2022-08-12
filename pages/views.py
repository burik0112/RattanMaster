from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from index.models import Product, Responsible
from pages.models import Category


# class AboutView(ListView):
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         qs = Product.objects.order_by('-pk')
#
#         q = self.request.GET.get('q')
#
#         if q:
#             qs = qs.filter(title__icontains=q)
#         return qs


class CategoryView(ListView):
    template_name = 'categories.html'
    queryset = Category.objects.order_by('-pk')


class CalendarView(TemplateView):
    template_name = 'responsible_person.html'
    queryset = Category.objects.order_by('-pk')


class EquipmentsView(ListView):
    template_name = 'catalog_category.html'
    queryset = Category.objects.all()

def CatProList(request, pk):
    query = Product.objects.filter(category_id__id=pk)
    print(query)
    return render(request, 'index.html', {'object': query})


class ResponsibleView(ListView):
    template_name = 'responsible_person.html'
    queryset = Responsible.objects.order_by('-pk')


class AmountView(ListView):
    template_name = 'categories.html'

    def get_queryset(self):
        qs = Category.objects.order_by('-pk')
        return qs
