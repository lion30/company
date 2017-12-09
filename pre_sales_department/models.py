from django.db import models
from sales_department.models import Contract_clue
from human_res_department.models import Employee

class Presale(models.Model):
	project_number = models.ForeignKey(Contract_clue,to_field=Contract_clue.project_number, on_delete=models.PROTECT)
	project_name = models.ForeignKey(Contract_clue, on_delete=models.CASCADE)
	material_count = models.IntegerField('供货数量')
	bid_price = models.IntegerField('投标价格')
	employee_name = models.ForeignKey(Employee, to_field=Employee.employee_name)
	employee_number = models.ForeignKey(Employee, to_field=Employee.employee_id)
	#material_number
	#material_name



