# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 04:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetComponentAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asset-Component Assembly',
                'verbose_name_plural': 'Asset-Component Assemblies',
            },
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('serial', models.CharField(db_index=True, max_length=64)),
                ('description', models.TextField(blank=True, default='', help_text='Describe the item.', null=True)),
                ('mac_address', models.CharField(db_index=True, max_length=17, unique=True)),
                ('notes', models.TextField(blank=True, default='', help_text='General notes on this Asset', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, default='', help_text='Cases for when this category should be used')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True, default='', help_text='Describe the item.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Component',
                'verbose_name_plural': 'Components',
            },
        ),
        migrations.CreateModel(
            name='MakeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(db_index=True, max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Makers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=64, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=16, unique=True)),
                ('description', models.CharField(max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp that this record was submitted (user time).')),
                ('task_date', models.DateTimeField(help_text='Date of issue, if different from today.', null=True)),
                ('original_location', models.CharField(db_index=True, max_length=32)),
                ('task_description', models.TextField(help_text='Description of the problem with this item')),
                ('fix_description', models.TextField(blank=True, help_text='Description of actions taken to resolve the task')),
                ('management_comments', models.TextField(blank=True, help_text='Additional findings by management')),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(help_text='Asset ID associated with this Task', on_delete=django.db.models.deletion.PROTECT, related_name='asset_task_ref', to='rttApp.Assets')),
                ('replacement_asset', models.ForeignKey(blank=True, help_text='Asset ID of item that was placed as a replacement', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset_replacement_task_ref', to='rttApp.Assets')),
                ('resolved_by_user', models.ForeignKey(blank=True, help_text='User that resolved this task', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_task_resolved_ref', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(help_text='Task state', on_delete=django.db.models.deletion.PROTECT, to='rttApp.States')),
                ('submitted_by_user', models.ForeignKey(help_text='User that submitted this Task', on_delete=django.db.models.deletion.PROTECT, related_name='user_task_submitted_ref', to=settings.AUTH_USER_MODEL)),
                ('task_category', models.ForeignKey(help_text='Task/Issue Category', on_delete=django.db.models.deletion.PROTECT, to='rttApp.Categories')),
            ],
            options={
                'verbose_name': 'Repair Task',
                'verbose_name_plural': 'Repair Tasks',
            },
        ),
        migrations.AddField(
            model_name='makemodel',
            name='make',
            field=models.ForeignKey(help_text='Manufacturer', on_delete=django.db.models.deletion.PROTECT, related_name='maker_model_ref', to='rttApp.Makers'),
        ),
        migrations.AddField(
            model_name='components',
            name='model',
            field=models.ForeignKey(help_text='Make/Model', on_delete=django.db.models.deletion.PROTECT, related_name='makemodel_component_ref', to='rttApp.MakeModel'),
        ),
        migrations.AddField(
            model_name='assets',
            name='model',
            field=models.ForeignKey(help_text='Make/Model', on_delete=django.db.models.deletion.PROTECT, related_name='makemodel_asset_ref', to='rttApp.MakeModel'),
        ),
        migrations.AddField(
            model_name='assetcomponentassembly',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_assembly_ref', to='rttApp.Assets'),
        ),
        migrations.AddField(
            model_name='assetcomponentassembly',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='component_assembly_ref', to='rttApp.Components'),
        ),
        migrations.AlterUniqueTogether(
            name='makemodel',
            unique_together=set([('make', 'model_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='assets',
            unique_together=set([('serial', 'model')]),
        ),
    ]
