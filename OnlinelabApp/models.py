from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=10)


# 评分表
class ScoreTable(models.Model):
    # 解决方案名
    solution_name = models.CharField(max_length=100, default="", primary_key=True)
    # 公司名
    company_name = models.CharField(max_length=20, default="")
    # 评分人员
    judges = models.CharField(max_length=20, default="")
    # 填写日期
    date = models.CharField(max_length=50, default="")
    # 行业类型
    business_type = models.CharField(max_length=20, default="")
    # 业务类型
    industry_type = models.CharField(max_length=20, default="")
    # 总得分
    total_score = models.IntegerField(default=0)


# 分值记录表
class DetailScore(models.Model):
    # 解决方案名
    solution_name = models.ForeignKey("ScoreTable",  on_delete=models.CASCADE)
    # solution_name = models.CharField(max_length=100, default="")
    # 题目序号
    seq = models.IntegerField(default=0)
    # 得分
    score = models.IntegerField(default=0)
    unique_together = ("solution_name", "seq")


