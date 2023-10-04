from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Users
# from .form import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import AdminPasswordChangeForm

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        ('authenticate', {'fields': ('email', 'password')}),
        ('personal info', {'fields': ('full_name', 'mobile_phone')}),
        ('permissions', {'fields': ('is_staff', 'is_active')}),
        ('important data', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ("email", "mobile_phone", "full_name", "is_staff")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "full_name", "last_name", "mobile_phone")
    ordering = ('email', )
    form = UserChangeForm
    add_form = UserCreationForm
    filter_horizontal = []