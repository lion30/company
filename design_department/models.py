from django.db import models
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Contract(models.Model):
    project_number = models.ForeignKey(
        Contractclue,
        related_name=Contractclue.project_number,
        on_delete=models.PROTECT,
        verbose_name='合同号')
    project_name = models.ForeignKey(
        Contractclue,
        on_delete=models.PROTECT,
        verbose_name='合同名称'
    )
    sign_time = models.DateField('签订时间')
    contract_price = models.IntegerField('合同金额')
    contact_person = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name=Employee.employee_name,
        verbose_name='销售联系人')
    delivery_time = models.DateField('交货时间')
    material_count = models.IntegerField('供货数量')
    material_number = models.ForeignKey(
        Supplier,
        to_field=Supplier.material_number,
        on_delete=models.CASCADE,
        verbose_name='物料编号'
    )
    material_name = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        to_field=Supplier.material_name,
        verbose_name='物料名称'
    )



