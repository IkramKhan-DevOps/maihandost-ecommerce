from django.urls import path, include
from .views import (
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    DashboardView
)

app_name = "admins"
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/add/', CategoryListView.as_view(), name='category-create'),
    path('category/<int:pk>/change/', CategoryListView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryListView.as_view(), name='category-delete'),

]
