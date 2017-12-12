from django.apps import AppConfig
from django.contrib import admin
from .models import Employee


class HumanResDepartmentConfig(AppConfig):
    name = 'human_res_department'

class Human_res_admin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_age', 'enter_company_time',
                    'employee_department', 'staff_seniorty', 'employee_position',)
    actions = 