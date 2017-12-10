from django.db import models
from sales_department.models import Contract_clue
from human_res_department.models import Employee
from purchase_department.models import supplier_table

class Contract_table(models.Model):
    project_number = models.ForeignKey(
		Contract_clue,
		related_name=Contract_clue.project_number,
		on_delete=models.PROTECT,
		verbose_name='合同号')
    project_name = models.ForeignKey(
		Contract_clue,
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



