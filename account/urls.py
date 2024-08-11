from django.urls import path
from . import views


urlpatterns = [
    # -----------------------LOGIN-SYSTEM-------------------------- #
    # this url path for login user.
    path('login', views.login_user, name='login-user'),
    # this url path for register new user.
    path('signup', views.register_user, name='register-user'),
    # this url path for logout user.
    path('logout', views.logout_user, name='logout-user'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forget-password', views.forget_password, name='forget-password'),
    path('password-validate/<uidb64>/<token>/', views.password_validate, name='password-validate'),
    path('reset-password', views.reset_password, name='reset-password'),
    # ---------------------ADMIN-DASHBOARD------------------------- #
    path('admin/dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('product/add/', views.add_product, name='add-product'),
    path('view/product/list/', views.view_product, name='view-product'),
    path('edit/product/<str:product_id>/', views.edit_product, name='edit-product'),
    path('delete/product/<str:product_id>/', views.delete_product, name='delete-product'),
]