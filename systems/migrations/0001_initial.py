# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Name')),
                ('x', models.FloatField(verbose_name='Coordinate X')),
                ('y', models.FloatField(verbose_name='Coordinate Y')),
                ('z', models.FloatField(verbose_name='Coordinate Z')),
                ('eddb_id', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
            },
        ),
    ]
