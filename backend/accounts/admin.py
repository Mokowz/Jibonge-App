from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'is_active')
    # search_fields = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'email')
    # filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.unregister(Group)