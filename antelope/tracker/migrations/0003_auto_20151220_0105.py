# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20151219_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_invite',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invites',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='member_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='paranoia_level',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]
