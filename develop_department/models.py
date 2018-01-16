from django.db import models
from sales_department.models import Contractclue

class Develop_project(models.Model):
    """研发部工程数据库"""
    project_info = models.ForeignKey(Contractclue,
                                     related_name='project_info_develop',
                                     on_delete=models.CASCADE,
                                     verbose_name='研发项目信息')
    project_requirement = models.CharField(max_length=500)



class Develop_product(object):
    """研发部产品数据库"""
    
