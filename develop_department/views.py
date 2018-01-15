from django.shortcuts import render
from django.views.generic import View


class DevelopView(View):
    """研发部view"""
    def init_data(self):
