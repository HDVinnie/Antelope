# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20151220_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('login', models.DateTimeField()),
                ('ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(to='tracker.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userlogins',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserLogins',
        ),
    ]
