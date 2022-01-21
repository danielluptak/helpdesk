from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'is_it', 'is_customer', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'is_it', 'is_customer',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'is_it', 'is_customer',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)