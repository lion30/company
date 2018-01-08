from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Contractclue


class SalesIndex(View):
    template_name = 'sales.html'
    # def init_data(self):
    #     self.contract_clue = Contractclue.objects.all()

    def get(self, request):
        contract_clue = Contractclue.objects.all()
        return render(request, self.template_name, {'contract_clues': contract_clue})

