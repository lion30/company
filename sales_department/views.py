from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Contractclue


class Sales_index(View):
    def init_data(self):
        contract_clue = Contractclue.objects.all()
    def get(self):
        self.init_data(contract_clue)
    template_name = 'sales.html'


    return render(request, template_name)
