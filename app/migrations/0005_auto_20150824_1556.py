# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150814_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
