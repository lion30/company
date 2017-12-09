from django.db import models

class Contract_clue(models.Model):
	project_number = models.CharField('项目编号', max_length=40)
	project_name = models.CharField('项目名称', max_length=200)
	clue_source = models.CharField('项目来源', max_length=200)
	belong_industry = models.CharField('所属行业',choices=(
		(0, '火电'),
		(1, '水电'),
		(2, '电网'),
		(3, '核电'),
		(4, '化工'),
		(5, '轨道交通')))
	at_stage = models.CharField('所处阶段',choices=(
		(0, '市场前期'),
		(1, '售前阶段'),
		(2,'设计阶段'),
		(3, '生产采购阶段'),
		(4, '测试阶段'),
		(5, '出厂阶段'),
		(6,'现场调试阶段'),
		(7, '已投运'),
		(8,'暂停阶段')))
	next_plan = models.CharField('下一步工作',max_length=400)
	estimate_constract = models.IntegerField('项目预估合同额')
	intro_situation = models.CharField('项目情况简述')
	estabish_time = models.DateField(auto_now_add=True)
	last_update_time = models.DateField(auto_now=True)
