from django.db import models

class Department(models.Model):
    department = models.CharField('部门', max_length=40)

class Employee(models.Model):
    empolyee_id = models.IntegerField('员工编号')
