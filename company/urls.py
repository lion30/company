"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('design/', include('design_department.urls')),
    # path('develop/', include('develop_department.urls')),
    # path('engineer/', include('develop_department.urls')),
    # path('human_res/', include('human_res_department.urls')),
    # path('integrated/', include('integrated_department.urls')),
    # path('marketing/', include('marketing_department.urls')),
    # path('pre_sale/', include('pre_sales_department.urls')),
    # path('product/', include('product_department.urls')),
    # path('purchase/', include('purchase_department.urls')),
    # path('quality/', include('quality_department.urls')),
    path('sales/', include('sales_department.urls')),
    # path('tech_support/', include('tech_support_department.urls')),
    # path('test/', include('test_department.urls')),
]
