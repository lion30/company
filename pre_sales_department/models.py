from django.db import models
from sales_department.models import Contract_clue
from human_res_department.models import Employee
from purchase_department.models import supplier_table

class Presale(models.Model):
    project_number = models.ForeignKey(Contract_clue,to_field=Contract_clue.project_number, on_delete=models.PROTECT)
    project_name = models.ForeignKey(Contract_clue, on_delete=models.CASCADE)
    material_count = models.IntegerField('供货数量')
    bid_price = models.IntegerField('投标价格')
    employee_name = models.ForeignKey(Employee, to_field=Employee.employee_name)
    employee_number = models.ForeignKey(Employee, to_field=Employee.employee_id)
    material_number = models.ForeignKey(
		supplier_table,
		to_field=supplier_table.material_number,
		on_delete=models.CASCADE,
		verbose_name='物料编号'
	)
    material_name = models.ForeignKey(
		supplier_table,
		on_delete=models.CASCADE,
		to_field=supplier_table.material_name,
		verbose_name='物料名称'
	)
    purchase_price = models.ForeignKey(
		supplier_table,
		on_delete=models.CASCADE,
		to_field=supplier_table.purchase_price,
		verbose_name='采购价格'
	)




