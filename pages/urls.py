from django.urls import path
from django.contrib.auth.decorators import login_required
from pages.views import AboutView, CategoryView, CalendarView, RegisterView, RecoverView, TableView, \
    CardView, AdminView

app_name = 'pages'

urlpatterns = [
    path('', login_required(AboutView.as_view()), name='main'),
    path('cat/', CategoryView.as_view(), name='category'),
    path('calendar/', login_required(CalendarView.as_view()), name='calendar'),
    # path('axasx/', LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('calendar/', RecoverView.as_view(), name='recover'),
    path('tables/', TableView.as_view(), name='table'),
    path('card/', CardView.as_view(), name='cards'),
    path('admin-add/', AdminView.as_view()),

]
