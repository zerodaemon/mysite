# coding=utf-8
# 模型

import datetime
from django.db import models
from django.utils import timezone


# Question 类
class Question(models.Model):
    question_text = models.CharField(max_length=200)   # 问题内容
    pub_date = models.DateTimeField('date published')  # 发布日期

    def __unicode__(self):                             # 给 Question 都添加一个 __unicode__() 方法
        return self.question_text

    def was_published_recently(self):                # 定义虚拟字段
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'              # 排序以发布日期为准
    was_published_recently.boolean = True                              # 显示为图形模式
    was_published_recently.short_description = 'Published recently?'   # 重定义字段显示名称

class Choice(models.Model):
    question = models.ForeignKey(Question)       # 答案关联的问题
    choice_text = models.CharField(max_length=200)  # 答案内容
    votes = models.IntegerField(default=0)    # 答案投票

    def __unicode__(self):              # 给 Choice 都添加一个 __unicode__() 方法
        return self.choice_text