# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20151220_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TorrentTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tag', models.ForeignKey(to='tracker.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogins',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('login', models.DateTimeField()),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AddField(
            model_name='torrent',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='torrent',
            name='leechers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='torrent',
            name='seeders',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='torrent',
            name='size',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='user',
            name='account_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='torrents_downloaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='torrents_uploaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userlogins',
            name='user',
            field=models.ForeignKey(to='tracker.User'),
        ),
        migrations.AddField(
            model_name='torrenttag',
            name='torrent',
            field=models.ForeignKey(to='tracker.Torrent'),
        ),
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(to='tracker.User'),
        ),
        migrations.AddField(
            model_name='report',
            name='reported_torrent',
            field=models.ForeignKey(to='tracker.Torrent'),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.ForeignKey(to='tracker.User'),
        ),
    ]
