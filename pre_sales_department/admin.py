from django.contrib import admin
from .models import Presale


class Pre_sale_Admin(admin.ModelAdmin):
    list_display = ("project_info", "material_info", "bid_price", "employee_presale", "bid_open_time","material_count")
    actions = ["make_picked"]
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("project_info", "material_info", "bid_price")}),
        ("高级", {"classes": ("collapse", ), "fields": ("employee_presale", "bid_open_time", "material_count")})
    )


admin.site.register(Presale, Pre_sale_Admin)
