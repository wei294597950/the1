# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class deletelog(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name='删除日志'
        verbose_name_plural=verbose_name

    class Meta:
        permissions=(
            ("检索", "检索权限"),
            ("新增", "新增权限"),
            ("删除", "删除权限"),
            ("修改", "修改权限"),
            ("恢复", "恢复权限"),


        )


class restore(models.Model):
    date = models.DateTimeField()
    user = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    qaid = models.CharField(max_length=50,primary_key=True)
    content = models.CharField(max_length=100)
    class Meta:
        verbose_name='恢复'
        verbose_name_plural=verbose_name


class data_table(models.Model):
    query = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    query_count = models.IntegerField()
    count = models.IntegerField()
    good_count = models.IntegerField()
    bad_count = models.IntegerField()
    export_tag = models.IntegerField()

class data_log(models.Model):
    qaid = models.IntegerField()
    query = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    result = models.IntegerField()
    datetime = models.DateTimeField()

class the_log(models.Model):
    qaid = models.IntegerField()
    query = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    result = models.IntegerField()
    datetime = models.DateTimeField()