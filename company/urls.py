"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from .views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^design/', include('design_department.urls')),
    url(r'^develop/', include('develop_department.urls')),
    url(r'^engineer/', include('develop_department.urls')),
    url(r'^human_res/', include('human_res_department.urls')),
    url(r'^integrated/', include('integrated_department.urls')),
    url(r'^marketing/', include('marketing_department.urls')),
    url(r'^pre_sale/', include('pre_sales_department.urls')),
    url(r'^pruduct/', include('pruduct_department.urls')),
    url(r'^purchase/', include('purchase_department.urls')),
    url(r'^quality/', include('quality_department.urls')),
    url(r'^sales/', include('sales_department.urls')),
    url(r'^tech_support/', include('tech_support_department.urls')),
    url(r'^test/', include('test_department.urls')),
]
