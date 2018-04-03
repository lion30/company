from django.contrib import admin
from .models import Contractclue, Contract, TechnicalAgreement


class ClueAdmin(admin.ModelAdmin):
    list_display = (
        'clue_number', 'clue_name', 'clue_source',
        'belong_industry', 'clue_area', 'at_stage',
        'next_plan', 'estimate_contract', 'intro_situation',
        'establish_time', 'last_update_time', 'establish_person', "clue_status", 'customer_company', 'main_customer_name',
        'main_customer_contact', 'main_customer_post', 'customer_name',
        'customer_contact', 'customer_post', 'clue_remark', 'competitor_1',
        'competitor_2', 'competitor_3', 'success_rate',
    )
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("clue_number", "clue_name", "clue_source", "belong_industry", "clue_area", "at_stage", "next_plan", "estimate_contract", "intro_situation", "establish_person", "clue_status", )}),
        ("高级", {"classes": ("collapse", ), "fields": ("customer_company", "main_customer_name", "main_customer_contact", "customer_post", "clue_remark", "competitor_1", "competitor_2", "competitor_3", "success_rate", )})
    )
    readonly_fields = ("establish_time", "last_update_time")


admin.site.register(Contractclue, ClueAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "project_number", "project_name", "contract_amount",
        "contract_payment", "customer_company", "customer_level",
        "belong_industry", "project_area", "sales_person",
        "approval_person", "project_stage", "project_status", "sign_time",
        "contract_file", "supply_time", "is_contract_clue", "contract_clue",
        "business_leader", "business_post", "business_leader_contact",
        "technical_leader", "technical_leader_post", "technical_leader_contact",
        "contract_receipt", "contract_remark",
    )
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("project_number", "project_name", "contract_amount", "contract_payment", "customer_company", "customer_level", "belong_industry", "project_area", "sales_person", "approval_person", "project_stage", "project_status", "contract_file", )}),
        ("高级", {"classes": ("", ), "fields": ("is_contract_clue", "contract_clue", "business_leader", "business_post", "business_leader_contact", "technical_leader", "technical_leader_post", "technical_leader_contact", "contract_receipt", "contract_remark",)})
        )
    readonly_fields = ("supply_time", "sign_time")


admin.site.register(Contract, ContractAdmin)


class TechnicalAgreementAdmin(admin.ModelAdmin):
    list_display = (
        "project_info", "presale_info", "customer_owner",
        "receive_request_time", "technical_agreement_signtime",
        "technical_agreement_doc", "project_process", "project_status",
        "delivery_receiver", "receivering_address", "receiver_contact",)

    actions = ['make_picked']

    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("project_info", "presale_info", "customer_owner", "technical_agreement_doc", "project_process", "project_status",)}),
        ("高级", {"classes": ("", ), "fields": ("delivery_receiver", "receivering_address", "receiver_contact",)})
        )
    readonly_fields = ("receive_request_time", "technical_agreement_signtime",)


admin.site.register(TechnicalAgreement, TechnicalAgreementAdmin)
