from django.contrib import admin
from .models import Meeting_room, Company_issue


class Company_Issue_Admin(admin.ModelAdmin):
    list_display = ("article_name", "article_author", "clicks_count", "article_content",
                    "article_establish_time", "article_status")
    fieldsets = (
        ("基本", {"classes": ("", ), "fields": ("article_name", "article_author", "article_establish_time",
                                              "article_status")}),
        ("高级", {"classes": ("collapse", ), "fields": ("clicks_count", "article_content")})
    )


class Meeting_Admin(admin.ModelAdmin):
    list_display = ("conference_applicant", "conference_start_time", "conference_end_time",
                    "conference_theme", "conference_participant", "room_status", "room_applicant_status")
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("conference_applicant", "conference_theme",
                                             "conference_start_time", "conference_end_time")}),
        ("高级", {"classes": ("collapse", ), "fields": ("conference_participant", "room_status",
                                                      "room_applicant_status")})
    )


admin.site.register(Meeting_room, Meeting_Admin)
admin.site.register(Company_issue, Company_Issue_Admin)