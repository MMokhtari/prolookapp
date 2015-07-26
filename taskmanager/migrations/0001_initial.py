# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('AuthAccount', '0005_auto_20150209_2111'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, blank=True, default='Title')),
                ('content', models.TextField(default='')),
                ('status', models.CharField(max_length=20, blank=True, choices=[('PENDING', 'Pending'), ('DONE', 'Done'), ('CANCELED', 'Canceled'), ('PROSTPOND', 'Prostpond')], null=True)),
                ('progression', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('is_repeatable', models.BooleanField(default=False)),
                ('repeat_every', models.CharField(max_length=20, blank=True, choices=[('DAY', 'day'), ('MONTH', 'Month')], null=True)),
                ('repeat_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], default=1)),
                ('is_event', models.BooleanField(default=False)),
                ('is_prostpondable', models.BooleanField(default=True)),
                ('is_referable', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('task', models.ForeignKey(to='taskmanager.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskReport',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30, blank=True, default='')),
                ('content', models.TextField(default='')),
                ('task', models.ForeignKey(to='taskmanager.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskReportComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('taskreport', models.ForeignKey(to='taskmanager.TaskReport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30, blank=True, default='')),
                ('description', models.CharField(max_length=60, blank=True, default='')),
                ('color', models.CharField(max_length=20, default='#342321')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskTrack',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('refered_date', models.DateTimeField(auto_now_add=True)),
                ('refered_to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(to='taskmanager.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, to='taskmanager.TaskTag', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(to='AuthAccount.Team', blank=True, default=None, null=True),
            preserve_default=True,
        ),
    ]
