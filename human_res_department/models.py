from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    department_choices = (
        (0, '销售部'),
        (1, '售前部'),
        (2, '设计部'),
        (3, '采购部'),
        (4, '生产部'),
        (5, '质量管理部'),
        (6, '综合管理部'),
        (7, '市场部'),
        (8, '工程部'),
        (9, '技术支持部'),
        (10, '研发部'),
        (11, '测试部'),
        (12, '人力资源部'),
        (13, '财务部'),
    )

    position_choices = (
        (0, '售前工程师'),
        (1, '设计工程师'),
        (2, '销售经理'),
        (3, '市场专员'),
        (4, '库房管理员'),
        (5, '部门经理'),
        (6, '部门副经理'),
        (7, '大区经理'),
        (8, '省区经理'),
        (9, '生产副总经理'),
        (10, '销售副总经理'),
        (11, '市场副总经理'),
        (12, '生产总经理'),
        (13, '销售总经理'),
        (14, '市场总经理'),
        (15, '综合管理部副经理'),
        (16, '综合管理部经理'),
        (17, '总经理'),
        (18, '总经理助理'),
        (19, '现场服务工程师'),
    )
    employee_id = models.IntegerField('员工编号', unique=True)
    employee_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="员工姓名")
    employee_age = models.IntegerField('员工年龄')
    enter_company_time = models.DateField('入职时间')
    employee_department = models.PositiveSmallIntegerField('所属部门', choices=department_choices)
    staff_seniority = models.PositiveSmallIntegerField('工龄')
    employee_position = models.PositiveSmallIntegerField('所属职位', choices=position_choices)

    def __str__(self):
        return self.employee_id

    class Meta:
        verbose_name = '人力资源部'
        verbose_name_plural = '人力资源部'

