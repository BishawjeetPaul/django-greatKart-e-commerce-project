from django.urls import path
from . import views


urlpatterns = [
    # this url path for showing store page.
    path('', views.store, name='store'),
    # this url path for showing products by category.
    path('category/<slug:category_slug>/', views.store, name='product-by-category'),
    # this url path for showing products details.
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product-detail'),
    # this url path for search the products.
    path('search/', views.search, name='product-search'),
]