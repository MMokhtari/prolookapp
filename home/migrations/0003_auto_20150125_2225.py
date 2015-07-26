# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150125_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='ip',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='refer',
            field=models.CharField(default='None', max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='user_agent',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
