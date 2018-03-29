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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sales/', views.salesIndex.as_view()),
    url(r'^cluecreate/', views.salesClueCreate.as_view()),
    url(r'^cluehistory/', views.salesClueHistory.as_view()),
    url(r'^cluemanagement/', views.salesClueManagement.as_view()),
    url(r'^clueupdate/', views.salesClueUpdate.as_view()),
    url(r'^salesclue/', views.salesClue.as_view()),
    url(r'^contractmanagement/', views.salesContractManagement.as_view()),
    url(r'^contractupdate/', views.salesContractUpdate.as_view()),
    url(r'^salescontract/', views.salesContract.as_view()),
    url(r'^technicalagreement/', views.technicalAgreement.as_view()),
    url(r'^technicalagreementmanagement/', views.technicalAgreementManagement.as_view()),
]
