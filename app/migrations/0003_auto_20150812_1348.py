# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_position_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
