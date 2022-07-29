from django.urls import path

from pages.views import AboutView, CategoryView, CalendarView, LoginView, RegisterView, RecoverView, TableView, CardView

app_name = 'pages'

urlpatterns = [
    path('', AboutView.as_view(), name='main'),
    path('cat/', CategoryView.as_view(), name='category'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('calendar/', RecoverView.as_view(), name='recover'),
    path('tables/', TableView.as_view(), name='table'),
    path('card/', CardView.as_view(), name='card'),

]
