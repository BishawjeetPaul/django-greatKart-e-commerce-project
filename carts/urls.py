from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/cart/<int:product_id>/', views.add_cart, name='add-cart'),
    path('remove/cart/<int:product_id>/', views.remove_card, name='remove-cart'),
    path('remove/cart/item/<int:product_id>/', views.remove_cart_item, name='remove-cart-item'),
]