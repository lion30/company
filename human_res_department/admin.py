from django.contrib import admin
from .models import Employee

class Humanresadmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_age', 'enter_company_time',
                    'employee_department', 'staff_seniorty', 'employee_position')
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("employee_id", "employee_name", "employee_department", "employee_position")}),
        ("高级", {"classes": ("collapse", ),"fields": ("employee_age", "staff_seniorty", 'enter_company_time')})
    )

admin.site.register(Employee, Humanresadmin)