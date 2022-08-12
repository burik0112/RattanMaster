import imp
from django.urls import path
from .views import Base, Detail, SearchResultsView, IndexCustom, DeviceModels, ResponsiblePeople
app_name = 'pages'

urlpatterns = [
    path('index', IndexCustom, name='cards'),
    path('base/<int:pk>', Base, name='base'),
    path('base/<int:pk>/detail', Detail, name='detail'),
    path('models/', DeviceModels, name='models'),
    path('responsible-people/', ResponsiblePeople, name='responsible'),
    path('search', SearchResultsView.as_view(), name='search'),
]
