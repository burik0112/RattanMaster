import imp
from django.urls import path
from .views import Index, Base, Detail, SearchResultsView, IndexCustom, Categories, DeviceModels, ResponsiblePeople


urlpatterns = [
    path('', Index, name='index'),
    path('index', IndexCustom, name='index-custom'),
    path('base/<int:pk>', Base, name='base'),
    path('base/<int:pk>/detail', Detail, name='detail'),
    path('categories', Categories, name='categories'),
    path('models', DeviceModels, name='models'),
    path('responsible-people', ResponsiblePeople, name='responsible'),
    path('search', SearchResultsView.as_view(), name='search'),
]
