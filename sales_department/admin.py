from django.contrib import admin
from .models import Contractclue

class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'project_number', 'project_name', 'clue_source', 'belong_industry', 'at_stage', 'next_plan',
        'estimate_constract', 'estabish_time', 'last_update_time', 'estabish_person', "intro_situation"
    )
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("project_number", "project_name", "estabish_person",
                                              "at_stage", "next_plan", "estimate_constract")}),
        ("高级", {"classes": ("collapse", ), "fields": ("clue_source", "belong_industry", "intro_situation")})
    )
    readonly_fields = ("estabish_time", "last_update_time")

admin.site.register(Contractclue, SalesAdmin)