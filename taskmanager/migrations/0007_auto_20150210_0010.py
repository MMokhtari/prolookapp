# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0006_auto_20150210_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tagss',
            new_name='tags',
        ),
    ]
