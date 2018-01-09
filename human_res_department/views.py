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
        Employee_data = User.objects.all()
        return render(request, self.template_name, {'Employee_info': Employee_info,
                                                    'Employee_data': Employee_data})

