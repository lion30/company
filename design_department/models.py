from django.db import models
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Contract(models.Model):
    project_number = models.OneToOneField(
        Contractclue,
        to_field='project_number',
        on_delete=models.PROTECT,
        related_name='project_number_desi',
        verbose_name='合同号',
    )
    project_name = models.OneToOneField(
        Contractclue,
        on_delete=models.PROTECT,
        to_field='project_name',
        related_name='project_name_desi',
        verbose_name='合同名称',
    )
    sign_time = models.DateField('签订时间')
    contract_price = models.IntegerField('合同金额')
    contact_person = models.OneToOneField(
        Employee,
        on_delete=models.PROTECT,
        to_field='employee_name',
        related_name='contact_person_desi',
        verbose_name='销售联系人')
    delivery_time = models.DateField('交货时间')
    material_count = models.IntegerField('供货数量')
    material_number = models.OneToOneField(
        Supplier,
        to_field='material_number',
        on_delete=models.CASCADE,
        related_name='material_number_desi',
        verbose_name='物料编号'
    )
    material_name = models.OneToOneField(
        Supplier,
        on_delete=models.CASCADE,
        to_field='material_name',
        related_name='material_name_desi',
        verbose_name='物料名称'
    )
