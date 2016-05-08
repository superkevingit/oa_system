# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('writer', models.CharField(max_length=50, verbose_name='\u53d1\u5e03\u8005')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
            ],
        ),
    ]
