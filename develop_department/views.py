from django.shortcuts import render
from django.views.generic import View
from .models import Develop_product, Develop_project


class DevelopView(View):
    """研发部view"""
    template_name = 'index_develop.html'
    model_name = Develop_product

    def init_data(self):
        model_data = self.model_name.objects.all()

    def get(self, request):
        return render(request, self.template_name,
                      {"Develop_product": self.model_data})
