# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_data_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qaid', models.IntegerField()),
                ('query', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
