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
    """建立销售线索."""
    template_name = 'sales_clue_create.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueUpdate(View):
    """更新线索"""
    template_name = 'sales_clue_update.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueHistory(View):
    """线索历史."""
    template_name = 'sales_clue_history.html'

    def get(self, request):
        return render(request, self.template_name)


class salesClueManagement(View):
    """线索管理."""
    template_name = 'sales_clue_management.html'

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
    """docstring for 更新销售合同."""

    template_name = 'sales_contract_update.html'

    def get(self, request):
        return render(request, self.template_name)


class salesContract(View):
    """docstring for 销售合同管理."""

    template_name = 'sales_contract.html'

    def get(self, request):
        return render(request, self.template_name)


class technicalAgreementManagement(View):
    """docstring for 技术协议."""

    template_name = 'technical_agreement_management.html'

    def get(self, request):
        return render(request, self.template_name)


class technicalAgreement(View):
    """docstring for [技术协议]."""
    template_name = 'technical_agreement.html'

    def get(self, request):
        return render(request, self.template_name)
