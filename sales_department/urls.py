"""company path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.salesIndex.as_view()),
    path('cluecreate/', views.salesClueCreate.as_view()),
    path('cluehistory/<str:clue_number>/', views.salesClueHistory.as_view(), name='cluehistory'),
    path('cluemanagement/', views.salesClueManagement.as_view()),
    path('clueupdate/', views.salesClueUpdate.as_view()),
    path('salesclue/<int:clue_id>/', views.salesClue.as_view(), name='salesclue'),
    path('contractmanagement/', views.salesContractManagement.as_view()),
    path('contractupdate/', views.salesContractUpdate.as_view()),
    path('salescontract/', views.salesContract.as_view()),
    path('technicalagreement/', views.technicalAgreement.as_view()),
    path('technicalagreementmanagement/', views.technicalAgreementManagement.as_view()),
]
