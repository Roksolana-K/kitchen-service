from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, DishType, Dish


admin.site.register(DishType)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "dish_type",
        "price",
        "description",
    ]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "years_of_experience",
                )
            },
        ),
    )
