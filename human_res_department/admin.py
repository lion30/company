from django.contrib import admin
from .models import Employee
from .models import Department


class Humanresadmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_age', 'enter_company_time',
                    'employee_department', 'staff_seniority', 'employee_position')
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("employee_id", "employee_name", "employee_department",
                                             "employee_position")}),
        ("高级", {"classes": ("collapse", ), "fields": ("employee_age", "staff_seniority", 'enter_company_time')})
    )


admin.site.register(Employee, Humanresadmin)

class DepartmentAdmin(admin.ModelAdmin):
    """部门后台管理."""
    list_display = ('department_name',)
    actions = ['make_picked']
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("department_name",)}),
    )

admin.site.register(Department, DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
    """职位后台管理."""
    list_display = ("position_name", "position_remark")
    actions = ["make_picked"]
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("position_name", "position_remark")})
    )
