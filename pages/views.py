from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'index.html'


class CategoryView(TemplateView):
    template_name = 'pages-directory.html'


class CalendarView(TemplateView):
    template_name = 'calendar.html'
