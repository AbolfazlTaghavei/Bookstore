from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )

    #  (
    #     (None, {'fields': ('username', 'password', )}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age', )}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',  )}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined', )}),
    # )
    
    add_fieldsets = (
        (None, {
        'classes': ('wide', ),
        'fields': ('username', 'password1', 'password2', 'age', 'email' )
        }
        ),
    )

    