from django.db import models
from human_res_department.models import Employee
from django.contrib.auth.models import User


class Company_issue(models.Model):
    article_name = models.CharField("文章名称", max_length=200)
    article_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="article_author",
        verbose_name="文章作者"
    )
    clicks_count = models.PositiveSmallIntegerField("点击量")
    article_content = models.TextField("文章内容")
    article_establish_time = models.DateField("创建日期", auto_now=True)
    article_status = models.PositiveSmallIntegerField("文章状态", choices=((0, "正常"), (1, "删除")))

    def __str__(self):
        return self.article_name

    class Meta:
        verbose_name = "公司发文"
        verbose_name_plural = "公司发文"


class Meeting_room(models.Model):
    conference_applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="会议申请人"
    )
    conference_start_time = models.DateTimeField(verbose_name="会议开始时间")
    conference_end_time = models.DateTimeField(verbose_name="会议结束时间")
    conference_theme = models.CharField(verbose_name="会议主题", max_length=200, help_text="不超过50字")
    conference_participant= models.CharField(verbose_name="会议参与人", max_length=200)
    room_status = models.PositiveSmallIntegerField(verbose_name="会议室状态",
                                                   choices=((0, "可申请"), (1, "已预定"), (2, "不可用")),
                                                   default=0)
    room_applicant_status = models.PositiveSmallIntegerField(verbose_name="会议室申请状态",
                                                             choices=((0, "待审批"), (1, "审批通过"), (2, "审批未通过")),
                                                             default=0)

    def __str__(self):
        return self.conference_theme

    class Meta:
        verbose_name = "会议室申请"
        verbose_name_plural = "会议室申请"
