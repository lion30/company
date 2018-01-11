from django.views.generic import View
from django.shortcuts import render
from .models import Presale

class PreSaleView(View):
    """售前view"""
    template_name = "index_pre_sale.html"
    # def init_data(self):
    #     self.pre_sale_data = Presale.objects.all()
    def get(self, request):
        pre_sale_data = Presale.objects.all()
        return render(request, self.template_name, {"pre_sale_data": pre_sale_data})
