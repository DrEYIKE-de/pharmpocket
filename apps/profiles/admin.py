from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "gender",
        "title",
        "is_employee",
    ]
    list_display_links = [
        "pkid",
        "id",
        "user",
    ]
    search_fields = [
        "pkid",
        "gender",
        "is_employee",
        "title",
    ]


admin.site.register(Profile, ProfileAdmin)
