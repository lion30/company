from django.contrib import admin
from .models import Supplier, Store
class Supplier_Admin(admin.ModelAdmin):
    list_display = ("manufacturer", "manufacturer_level", "material_number", "material_name", "material_group",
                    "payment_method", "material_remarks", "discount_info", "material_unit", "supply_cycle",
                    "purchase_price")
    fieldsets = (
        ("基本",{"classes": ("", ),"fields": ("manufacturer", "manufacturer_level", "material_number",
                                            "material_name")}),
        ("高级", {"classes": ("collapse", ), "fields": ("material_group", "material_unit", "puchase_price",
                                                      "supply_cycle", "payment_method", "discount_info",
                                                      "material_remarks")})
    )

class Stroe_Admin(admin.ModelAdmin):
    list_display = ("material_number", "material_name", "material_unit", "material_group", "manufacturer",
                    "material_remarks", "inventory_quantity", "store_location")
    fieldsets = (
        ("基本", {"classes": ("", ),"fields":)})
    )
admin.site.register(Supplier, Store)
