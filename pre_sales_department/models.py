from django.db import models
from sales_department.models import Contractclue
from human_res_department.models import Employee
from purchase_department.models import Supplier


class Presale(models.Model):
    project_number = models.ForeignKey(Contractclue,to_field=Contractclue.project_number, on_delete=models.PROTECT)
    project_name = models.ForeignKey(Contractclue, on_delete=models.CASCADE)
    material_count = models.IntegerField('供货数量')
    bid_price = models.IntegerField('投标价格')
    employee_name = models.ForeignKey(Employee, to_field=Employee.employee_name)
    employee_number = models.ForeignKey(Employee, to_field=Employee.employee_id)
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
    purchase_price = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        to_field=Supplier.purchase_price,
        verbose_name='采购价格'
    )




