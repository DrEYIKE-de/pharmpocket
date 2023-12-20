from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User 
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["pkid", "id", "username", "email", "phone_number", "is_active", "is_superuser", "date_joined"]
    list_display_links = ["pkid", "username", "email"]
    list_filter = ["username", "email", "phone_number", "is_staff", "is_active",]
    search_fields = ["username", "email", "phone_number",]
    date_hierarchy = "date_joined"   
    fieldsets = (
        (
            _("Login Credentials",), {
                "fields": ("username", "password", )
            }
        ),
        (
            _("Personal Information",),
            {
                "fields": ("phone_number",),
            },
        ),
        (
            _("Groups and Permissions"), {
                "fields": ("is_active", "is_superuser", "is_staff", "groups", "user_permission",),
            },
        ),
        (
            _("Important dates"), {
                "fields": ("last_login", "date_joined",),
            }
        )
    )
    add_fieldsets = (
        None, {
            "class": "wide",
            "fields": ("username", "password1", "password2", "is_active", "is_staff",)
        },
    )


admin.site.register(User, CustomUserAdmin)