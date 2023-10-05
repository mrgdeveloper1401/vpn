from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Users
from .form import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import AdminPasswordChangeForm

@admin.register(Users)
class UsersAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("full_name", "mobile_phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("email", "mobile_phone", "full_name", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("mobile_phone", "full_name", "email")
    ordering = ("email",)
    readonly_fields = ('date_joined', )
    filter_horizontal = []