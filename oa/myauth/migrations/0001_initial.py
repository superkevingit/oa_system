# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u7528\u6237\u540d')),
                ('studentid', models.CharField(max_length=20, verbose_name='\u4e00\u5361\u901a\u53f7')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('tel', models.CharField(max_length=50, verbose_name='\u7535\u8bdd')),
                ('mail', models.EmailField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('is_active', models.BooleanField(default=1, verbose_name='\u6fc0\u6d3b')),
            ],
        ),
    ]
