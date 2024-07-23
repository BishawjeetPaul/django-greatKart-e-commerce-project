from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import Account


# class UserModel(UserAdmin):
#     pass

admin.site.register(Account)