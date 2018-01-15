from django.db import models
from django.contrib.auth.models import User
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Presale(models.Model):
    project_info = models.ForeignKey(
        Contractclue,
        related_name='project_info_presale',
        on_delete=models.PROTECT,
        verbose_name='项目信息'
    )
    material_info = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='物料信息',
        related_name='material_info_presale'
    )
    material_count = models.PositiveIntegerField('供货数量')
    bid_price = models.PositiveIntegerField('投标价格')
    employee_presale = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="presale_user",
        verbose_name="售前负责人"
    )
    bid_open_time = models.TimeField('开标时间')


    def __str__(self):
        return self.project_number

    class Meta:
        verbose_name = "售前支持部"
        verbose_name_plural = "售前支持部"
