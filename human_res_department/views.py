from django.views.generic import View
from django.shortcuts import render
from .models import Employee


class HumanRes(View):
    template_name = 'index_human.html'

    # def init_data(self):
    #     self.Employee_info = Employee.objects.all()

    def get(self, request):
        Employee_info = Employee.objects.all()
        return render(request, self.template_name, {'Employee_info': Employee_info})

