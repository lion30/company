from django.db import models
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Presale(models.Model):
    project_number = models.ForeignKey(
        Contractclue,
        to_field='project_number',
        related_name='project_number_pre_sale',
        on_delete=models.PROTECT,
        verbose_name='项目编号'
    )
    project_name = models.ForeignKey(
        Contractclue,
        to_field='project_name',
        related_name='project_name_pre_sale',
        on_delete=models.CASCADE,
        verbose_name='项目名称'
    )
    material_count = models.IntegerField('供货数量')
    bid_price = models.IntegerField('投标价格')
    employee_name = models.ForeignKey(
        Employee,
        to_field='employee_name',
        related_name='employee_name_pre_sale',
        verbose_name='员工姓名',
        on_delete=models.CASCADE
    )
    employee_number = models.ForeignKey(
        Employee,
        to_field='employee_id',
        related_name='employee_number_pre_sale',
        verbose_name='员工编号',
        on_delete=models.CASCADE
    )
    material_number = models.ForeignKey(
        Supplier,
        to_field='material_number',
        on_delete=models.CASCADE,
        verbose_name='物料编号',
        related_name='material_number_pre_sale'
    )
    material_name = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        to_field='material_name',
        verbose_name='物料名称',
        related_name='material_name_pre_sale'
    )
    purchase_price = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='采购价格',
        related_name='purchase_price_pre_sale'
    )

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "售前支持部"
        verbose_name_plural = "售前支持部"
