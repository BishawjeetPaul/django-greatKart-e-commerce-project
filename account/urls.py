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
    # this url path for user account dashboard.
    path('dashboard', views.dashboard, name='dashboard'),
    # this url path for user account activation.
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # this url path for user account forget password.
    path('forget-password', views.forget_password, name='forget-password'),
    # this url path for sent change password link for user email id. 
    path('password-validate/<uidb64>/<token>/', views.password_validate, name='password-validate'),
    # this url path for user account update old password to new-password.
    path('reset-password', views.reset_password, name='reset-password'),
    # ---------------------ADMIN-DASHBOARD------------------------- #
    # this url path for admin dashboard.
    path('admin/dashboard/', views.admin_dashboard, name='admin-dashboard'),
    # this url path for add product in application.
    path('product/add/', views.add_product, name='add-product'),
    # this url path for admin show all products. 
    path('view/product/list/', views.view_product, name='view-product'),
    # this url path for admin update products.
    path('edit/product/<str:product_id>/', views.edit_product, name='edit-product'),
    # this url path for admin delete products.
    path('delete/product/<str:product_id>/', views.delete_product, name='delete-product'),
]