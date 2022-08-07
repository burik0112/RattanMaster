from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from index.models import Product
from pages.models import Category


class AboutView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = Product.objects.order_by('-pk')

        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)
        return qs


class CategoryView(TemplateView):
    template_name = 'pages-directory.html'


class CalendarView(ListView):
    template_name = 'ui-images.html'
    queryset = Category.objects.order_by('-pk')


# class LoginView(CreateView, LoginRequiredMixin):
#     template_name = 'registration/login.html'

    # def post(self, request, *args, **kwargs):



class RegisterView(TemplateView):
    template_name = 'registration/registration_form.html'


class RecoverView(TemplateView):
    template_name = 'pages-recover.html'


class TableView(TemplateView):
    template_name = 'table.html'


class CardView(ListView):
    template_name = 'pages-directory.html'
    queryset = Category.objects.order_by('-pk')


class AdminView(TemplateView):
    template_name = 'admin-add.html'


class CatalogView(ListView):
    template_name = 'pages-directory.html'
    queryset = Category.objects.order_by('-pk')
