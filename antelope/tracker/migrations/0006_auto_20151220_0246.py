# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20151220_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='downloaded',
            field=models.DecimalField(decimal_places=2, max_digits=5, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='uploaded',
            field=models.DecimalField(decimal_places=2, max_digits=5, default=0),
        ),
    ]
