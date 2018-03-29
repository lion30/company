from django.contrib import admin
from .models import Supplier, Store


class Supplier_Admin(admin.ModelAdmin):
    list_display = ("manufacturer", "manufacturer_level", "material_number", "material_name", "material_group", "payment_method", "material_remarks_supplier", "discount_info", "material_unit", "supply_cycle", "purchase_price")
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("manufacturer", "manufacturer_level", "material_number",
                                              "material_name")}),
        ("高级", {"classes": ("collapse", ), "fields": ("material_group", "material_unit", "purchase_price",
                                                      "supply_cycle", "payment_method", "discount_info",
                                                      "material_remarks_supplier")})
    )


class Store_Admin(admin.ModelAdmin):
    list_display = ("material_number", "material_name", "material_unit", "material_group","material_type", "manufacturer", "" "material_remarks_store", "inventory_quantity", )
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("material_number", "inventory_quantity", "store_location")}),
        ("高级", {"classes": ("collapse", ), "fields": ("material_remarks_store", )})
    )


admin.site.register(Supplier, Supplier_Admin)
admin.site.register(Store, Store_Admin)
