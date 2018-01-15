from django.db import models
from human_res_department.models import Employee
from django.contrib.auth.models import User


class Contractclue(models.Model):
    project_number = models.CharField('项目编号', max_length=40, unique=True, db_index=True)
    project_name = models.CharField('项目名称', max_length=200, unique=True)
    clue_source = models.CharField('项目来源', max_length=200)
    belong_industry = models.SmallIntegerField('所属行业', choices=(
        (0, '火电'),
        (1, '水电'),
        (2, '电网'),
        (3, '核电'),
        (4, '化工'),
        (5, '轨道交通')))
    project_area = models.SmallIntegerField(verbose_name='项目区域',
                                            choices=(
                                                (0, '东北区'),
                                                (1, '华北区'),
                                                (2, '华中区'),
                                                (3, '华南区'),
                                                (4, '新疆'),
                                                (5, '西北区'))
                                            )
    at_stage = models.SmallIntegerField('所处阶段', choices=(
        (0, '市场前期'),
        (1, '售前阶段'),
        (2, '设计阶段'),
        (3, '生产采购阶段'),
        (4, '测试阶段'),
        (5, '出厂阶段'),
        (6, '现场调试阶段'),
        (7, '已投运'),
        (8, '暂停阶段')))
    next_plan = models.CharField('下一步工作', max_length=400)
    estimate_contract = models.IntegerField('项目预估合同额')
    intro_situation = models.CharField('项目情况简述', max_length=400)
    establish_time = models.DateField('线索建立时间', auto_now_add=True)
    last_update_time = models.DateField('线索更新时间', auto_now=True)
    establish_person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='establish_info',
        verbose_name='线索建立人')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "销售部"
        verbose_name_plural = "销售部"
