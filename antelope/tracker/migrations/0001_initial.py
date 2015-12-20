# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('passkey', models.CharField(max_length=60)),
                ('joined_date', models.DateField()),
                ('last_login', models.DateField()),
                ('uploaded', models.DecimalField(decimal_places=2, max_digits=5)),
                ('downloaded', models.DecimalField(decimal_places=2, max_digits=5)),
                ('torrents_uploaded', models.IntegerField()),
                ('torrents_downloaded', models.IntegerField()),
            ],
        ),
    ]
