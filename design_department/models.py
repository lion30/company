from django.db import models
from sales_department.models import Contract_clue
from human_res_department.models import Employee

class Contract_table(models.Model):
	project_number = models.ForeignKey(
		Contract_clue,
		related_name=Contract_clue.project_number,
		on_delete=models.PROTECT,
		verbose_name='合同号')
	project_name = models.ForeignKey(
		Contract_clue,
		on_delete=models.PROTECT,
		verbose_name='合同名称')
	sign_time = models.DateField('签订时间')
	contract_price = models.IntegerField('合同金额')
	contact_person = models.ForeignKey(
		Employee,
		on_delete=models.PROTECT,
		related_name=Employee.employee_name,
		verbose_name='销售联系人')
	delivery_time = models.DateField('交货时间')
	material_count = models.IntegerField('供货数量')
	#material_number
	#material_name


