from django.contrib import admin
from .models import Design


class Design_Admin(admin.ModelAdmin):
    list_display = ("project_number", "sign_time", "contract_person",
                    "delivery_time", "material_count", "material_number")
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("project_number", "material_number", "material_count")}),
        ("高级", {"classes": ("collapse", ), "fields": ("sign_time", "contract_person", "delivery_time")})
    )

admin.site.register(Design, Design_Admin)
