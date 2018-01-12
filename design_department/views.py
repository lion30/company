from django.shortcuts import render
from django.views.generic import View
from .models import Design


class DesignView(View):
    template_name = 'index_design.html'

    # def init_data(self):
    #     self.Design_data = Design.objects.all()

    def get(self, request):
        Design_data = Design.objects.all()
        return render(request, self.template_name,
                      {"Design_data": Design_data})
