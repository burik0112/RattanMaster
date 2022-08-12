from django.urls import path
from .views import Admin_index, CategoryCreateView, baseview, EquipmentCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, ResponsibleCreateView, ModelCreateView, SearchResultsView, AdminCategories, AdminCategoryEdit, \
    AdminCategoryDelete, AdminModels, AdminModelEdit, \
    AdminModelDelete, AdminResponsibles, AdminResponsibleEdit, AdminResponsibleDelete, AdminRooms, AdminRoomDetail

app_name = 'add'
urlpatterns = [
    path('admin-index/', Admin_index, name='admin-index'),
    path('admin-index/category-create', CategoryCreateView.as_view(), name='category-create'),
    path('admin-index/poka-base/<int:pk>', baseview, name='base-view'),
    path('admin-index/poka-base/<int:pk>/add-equipment', EquipmentCreateView, name='equipment-create'),
    path('admin-index/poka-base/<int:pk>/admin-detail-of-product', ProductDetailView, name='product-detail'),
    path('admin-index/poka-base/<int:pk>/product-update', ProductUpdateView, name='product-update'),
    path('admin-index/poka-base/<int:pk>/product-delete', ProductDeleteView, name='product-delete'),
    path('admin-index/responsible-create', ResponsibleCreateView.as_view(), name='responsible-create'),
    path('admin-index/model-create', ModelCreateView.as_view(), name='model-create'),
    path('admin/search', SearchResultsView.as_view(), name='admin-search'),
    path('admin/categories', AdminCategories, name='admin-categories'),
    path('admin/category-edit/<int:pk>', AdminCategoryEdit, name='category-edit'),
    path('admin/category-delete/<int:pk>', AdminCategoryDelete, name='category-delete'),
    path('admin/models', AdminModels, name='admin-models'),
    path('admin/model-edit/<int:pk>', AdminModelEdit, name='model-edit'),
    path('admin/model-delete/<int:pk>', AdminModelDelete, name='model-delete'),
    path('admin/responsibles', AdminResponsibles, name='admin-responsibles'),
    path('admin/responsible-delete/<int:pk>', AdminResponsibleDelete, name='responsible-delete'),
    path('admin/responsible-edit/<int:pk>', AdminResponsibleEdit, name='responsible-edit'),
    path('admin/rooms', AdminRooms, name='admin-rooms'),
    path('admin/room-detail/<int:pk>', AdminRoomDetail, name='admin-room-details'),
]
