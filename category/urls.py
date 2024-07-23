from django.urls import path
from . import views



urlpatterns = [
    path('category/view', views.view_category, name='view-category'),
    path('category/add/', views.add_category, name='add-category'),
    path('category/edit/<str:category_id>/', views.edit_category, name='edit-category'),
    path('category/delete/<str:category_id>/', views.delete_category, name='delete-category'),
]