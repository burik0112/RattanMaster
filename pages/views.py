from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from index.models import Product


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


class CalendarView(TemplateView):
    template_name = 'ui-images.html'


class LoginView(TemplateView):
    template_name = 'pages-login.html'


class RegisterView(TemplateView):
    template_name = 'registration/registration_form.html'


class RecoverView(TemplateView):
    template_name = 'pages-recover.html'


class TableView(TemplateView):
    template_name = 'table.html'


class CardView(TemplateView):
    template_name = 'card.html'
