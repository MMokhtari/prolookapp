# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20150209_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcomment',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='taskreport',
            old_name='created',
            new_name='created_at',
        ),
    ]
