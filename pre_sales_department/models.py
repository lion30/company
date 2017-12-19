from django.db import models
from django.contrib.auth.models import User
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Presale(models.Model):
    project_number = models.ForeignKey(
        Contractclue,
        related_name='project_number_pre_sale',
        on_delete=models.PROTECT,
        verbose_name='项目编号'
    )
    material_count = models.PositiveIntegerField('供货数量')
    bid_price = models.PositiveIntegerField('投标价格')
    employee_number = models.ForeignKey(
        Employee,
        related_name='employee_number_pre_sale',
        verbose_name='员工编号',
        on_delete=models.CASCADE
    )
    employee_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="员工姓名"
    )
    material_number = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='物料编号',
        related_name='material_number_pre_sale'
    )

    def __str__(self):
        return self.project_number

    class Meta:
        verbose_name = "售前支持部"
        verbose_name_plural = "售前支持部"
