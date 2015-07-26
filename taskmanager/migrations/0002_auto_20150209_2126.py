# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('created_at',)},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
    ]
