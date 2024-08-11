from django.urls import path
from . import views


urlpatterns = [
    # this url path for cart page.
    path('', views.cart, name='cart'),
    # this url path for add particular item in the cart.
    path('add/cart/<int:product_id>/', views.add_cart, name='add-cart'),
    # this url path for remove the cart.
    path('remove/cart/<int:product_id>/', views.remove_card, name='remove-cart'),
    # this url path for remove a item in the cart.
    path('remove/cart/item/<int:product_id>/', views.remove_cart_item, name='remove-cart-item'),
]