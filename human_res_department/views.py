from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Employee


class HumanRes(View):
    template_name = 'index_human.html'

    # def init_data(self):
    #     self.Employee_info = Employee.objects.all()

    def get(self, request):
        Employee_info = Employee.objects.all()
        datas = []
        for data in Employee_info:
            datas.append(data.employee_name.email)
            data.get_employee_position_display()
        print(datas)

        return render(request, self.template_name, {'Employee_info': Employee_info})

