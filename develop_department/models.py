from django.db import models
from engineering_department.models import

class Develop_project(models.Model):
    """研发部工程数据库"""
    project_info = models.ForeignKey(to, on_delete=None, related_name=None, related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)


class Develop_product(object):
    """研发部产品数据库"""
    
