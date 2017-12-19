from django.contrib import admin
from .models import Presale


class Pre_sale_Admin(admin.ModelAdmin):
    list_display = ("project_number", "material_count", "bid_price", "employee_number",
                    "employee_name", "material_number")
    actions = ["make_picked"]
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("project_number", "material_number",
                                             "material_count", "bid_price")}),
        ("高级", {"classes": ("collapse", ), "fields": ("employee_number", "employee_name")})
    )

admin.site.register(Presale, Pre_sale_Admin)
