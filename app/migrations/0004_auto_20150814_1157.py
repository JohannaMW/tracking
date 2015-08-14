# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150812_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
