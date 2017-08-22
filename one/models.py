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

class DecodeBase(models.Model):
    word = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)

    class Meta:
            db_table = 'decode_base'
            unique_together = (('word', 'tag'),)


class ProductionIntervene(models.Model):
    production_id = models.IntegerField()
    word = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    opertion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'production_intervene'
        unique_together = (('production_id', 'word', 'tag'),)


class ProductionDesc(models.Model):
    production_id = models.IntegerField(primary_key=True)
    production_name = models.CharField(unique=True, max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'production_desc'


class DecodeAll(models.Model):
    word = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)

    class Meta:
        db_table = 'decode_all'
        unique_together = (('word', 'tag'),)


class ProductionDiff(models.Model):
    user_id = models.CharField(max_length=128, blank=True, null=True)
    production_id = models.IntegerField()
    word = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    opertion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'production_diff'
        unique_together = (('production_id', 'word', 'tag'),)

class Tmp(models.Model):
    production_id = models.IntegerField()
    word = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    opertion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tmp'
        unique_together = (('production_id', 'word', 'tag'),)


class VersionBase(models.Model):
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'version_base'