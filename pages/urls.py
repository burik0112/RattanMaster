# from django.urls import path
# from django.contrib.auth.decorators import login_required
# from pages.views import CategoryView, ResponsibleView, AmountView, EquipmentsView, CatProList
#
# app_name = 'pages'
#
# urlpatterns = [
#     path('cat/<int:pk>/', login_required(CatProList), name='detail'),
#     # path('main/', login_required(AboutView.as_view()), name='main'),
#     path('cat/', CategoryView.as_view(), name='category'),
#     path('responsible/', login_required(ResponsibleView.as_view()), name='responsible'),
#     path('amounts/', AmountView.as_view(), name='amounts'),
#     path('', EquipmentsView.as_view(), name='cards'),
# ]
