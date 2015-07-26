# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20150209_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskreportcomment',
            old_name='created',
            new_name='created_at',
        ),
    ]
