from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Contractclue


class salesIndex(View):
    template_name = 'sales.html'
    # def init_data(self):
    #     self.contract_clue = Contractclue.objects.all()

    def get(self, request):
        contract_clue = Contractclue.objects.all()
        return render(request, self.template_name, {'contract_clues': contract_clue})


class salesClueCreate(View):
    template_name = 'sales_clue_create.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueHistory(View):
    template_name = 'sales_clue_history.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueManagement(View):
    template_name = 'sales_clue_management.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueUpdate(View):
    template_name = 'sales_clue_update.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClue(View):
    template_name = 'sales_clue.html'

    def get(self, request):
        return render(request, self.template_name)


class salesContractManagement(View):
    template_name = 'sales_contract_management.html'

    def get(self, request):
        return render(request, self.template_name)


class salesContractUpdate(View):
    """docstring for 创建销售线索."""

    template_name = 'sales_contract_update.html'

    def get(self, request):
        return render(request, self.template_name)


class saleContract(View):
    """docstring for [合同列表]"""

    template_name = 'sales_contract.html'

    def get(self, request):
        return render(request, self.template_name)
