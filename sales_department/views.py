from django.shortcuts import render


def sales_index(request):
    template_name = 'sales.html'
    return render(request, template_name)
