# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20160509_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oamessage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6fc0\u6d3b'),
        ),
    ]
