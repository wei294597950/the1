# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_restore'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('query_count', models.IntegerField()),
                ('count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('bad_count', models.IntegerField()),
                ('export_tag', models.IntegerField()),
            ],
        ),
    ]
