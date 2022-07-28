from django.urls import path

from pages.views import AboutView, CategoryView, CalendarView

app_name = 'pages'

urlpatterns = [
    path('', AboutView.as_view()),
    path('cat/', CategoryView.as_view(), name='category'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
]
