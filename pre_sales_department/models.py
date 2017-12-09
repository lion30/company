from django.db import models
from sales_department.models import Contract_clue

class Presale(models.Model):
	project_number = models.ForeignKey(Contract_clue,to_field=Contract_clue.project_number, on_delete=models.PROTECT)
	project_name = models.ForeignKey(Contract_clue,to_field=Contract_clue.project_name, on_delete=models.CASCADE)
	material_count = models.IntegerField('供货数量')


