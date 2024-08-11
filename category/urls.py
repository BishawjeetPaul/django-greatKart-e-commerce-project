from django.urls import path
from . import views



urlpatterns = [
    # this url path for show all the categories.
    path('category/view', views.view_category, name='view-category'),
    # this url path for add category.
    path('category/add/', views.add_category, name='add-category'),
    # this url path for edit particular category.
    path('category/edit/<str:category_id>/', views.edit_category, name='edit-category'),
    # this url path for delete particular category.
    path('category/delete/<str:category_id>/', views.delete_category, name='delete-category'),
]