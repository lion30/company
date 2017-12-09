from django.db import models

class Department(models.Model):
    department = models.CharField('部门', max_length=40)

class Position(models.Model):
    employee_position = models.CharField('职位', max_length=50)


class Employee(models.Model):
    employee_id = models.IntegerField('员工编号')
    employee_name = models.CharField('员工姓名',max_length=40)
    employee_age = models.IntegerField('员工年龄')
    enter_company_time = models.DateField('入职时间',auto_now_add=True)
    employee_department = models.ForeignKey(Department, on_delete= models.CASCADE)
    staff_seniorty = models.IntegerField('工龄')
    employee_position_fk = models.ForeignKey(Position, on_delete=models.CASCADE)
