from django.db import models
from sales_department.models import Contractclue
from purchase_department.models import Supplier
from django.contrib.auth.models import User


class Design(models.Model):
    project_number = models.ForeignKey(
        Contractclue,
        on_delete=models.CASCADE,
        related_name="project_number_desi",
        verbose_name='合同号',
    )
    sign_time = models.DateField('签订时间')
    contract_person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='设计负责人')
    delivery_time = models.DateField('交货时间')
    material_count = models.IntegerField('供货数量')
    material_number = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='material_number_desi',
        verbose_name='物料编号'
    )

    def __str__(self):
        return "设计部"

    class Meta:
        verbose_name = "设计部"
        verbose_name_plural = "设计部"
