from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import GroupAdmin as origGroupAdmin
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_of_birth',
                           'date_joined', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_supervisor')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register the modified GroupAdmin with the admin site
admin_site = admin.AdminSite(name='Live Furnish Admin')
admin.site.register(CustomUser, CustomUserAdmin)
