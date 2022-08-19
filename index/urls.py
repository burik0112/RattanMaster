import imp

from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Base, Detail, SearchResultsView, IndexCustom, DeviceModels, ResponsiblePeople, Categories, Room

app_name = 'pages'

urlpatterns = [
    path('index/', login_required(IndexCustom), name='cards'),
    path('base/<int:pk>', login_required(Base), name='base'),
    path('base/<int:pk>/detail', login_required(Detail), name='detail'),
    path('catogory/', login_required(Categories), name='category'),
    path('models/', login_required(DeviceModels), name='models'),
    path('rooms/', login_required(Room), name='rooms'),
    path('responsible-people/', login_required(ResponsiblePeople), name='responsible'),
    path('search', login_required(SearchResultsView.as_view()), name='search'),
]
