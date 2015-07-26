# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_auto_20150209_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tags',
            new_name='tagss',
        ),
    ]
