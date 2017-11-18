from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Makers(models.Model):
    """Stores unique Manufacturers"""
    maker = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.maker

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

class MakeModel(models.Model):
    """Makes a unique combination of makers and models - unique items are identified
    by the Assets model with serial numbers there."""
    make = models.ForeignKey(
        Makers,
        on_delete=models.PROTECT,
        help_text='Manufacturer',
        related_name='maker_model_ref'
    )
    model_name = models.CharField(db_index=True, max_length=64)
    description = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{make} {model}".format(
            make=self.make,
            model=self.model_name
        )

    class Meta:
        unique_together = (('make', 'model_name'),)
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

class Assets(models.Model):
    """Stores unique hardware assets"""
    model = models.ForeignKey(
        MakeModel,
        on_delete=models.PROTECT,
        help_text='Make/Model',
        related_name='makemodel_asset_ref'
    )
    number = models.PositiveIntegerField(unique=True)
    serial = models.CharField(db_index=True, max_length=64)
    description = models.TextField(default='', blank=True, null=True, help_text='Describe the item.')
    mac_address = models.CharField(db_index=True, max_length=17, unique=True)
    notes = models.TextField(default='', blank=True, null=True, help_text='General notes on this Asset')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{number} ({model} {serial})".format(
            number=self.number,
            model=self.model,
            serial=self.serial
        )

    class Meta:
        unique_together = (('serial', 'model'),)
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'


class Categories(models.Model):
    """Categories for tasks"""
    category = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='', blank=True, help_text='Cases for when this category should be used')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'


class States(models.Model):
    state = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Components(models.Model):
    model = models.ForeignKey(
        MakeModel,
        on_delete=models.PROTECT,
        help_text='Make/Model',
        related_name='makemodel_component_ref'
    )
    serial = models.CharField(max_length=64)
    notes = models.TextField(default='', blank=True, help_text='Describe the item.')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{model} {serial}".format(
            model=self.model,
            serial=self.serial
        )
    
    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'


class AssetComponentAssembly(models.Model):
    asset = models.ForeignKey(
        Assets,
        on_delete=models.CASCADE,
        related_name='asset_assembly_ref',
    )
    component = models.ForeignKey(
        Components,
        on_delete=models.PROTECT,
        related_name='component_assembly_ref'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{asset}-{component}".format(
            asset=self.asset.number,
            component=self.component
        )
    
    class Meta:
        verbose_name = 'Asset-Component Assembly'
        verbose_name_plural = "Asset-Component Assemblies"


class Tasks(models.Model):
    timestamp = models.DateTimeField(
        default=timezone.now,
        help_text='Timestamp that this record was submitted (user time).'
    )
    asset = models.ForeignKey(
        Assets,
        on_delete=models.PROTECT,
        help_text='Asset ID associated with this Task',
        related_name='asset_task_ref',
    )
    submitted_by_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text='User that submitted this Task',
        related_name='user_task_submitted_ref',
    )
    task_date = models.DateTimeField(null=True, help_text='Date of issue, if different from today.')
    original_location = models.CharField(db_index=True, max_length=32)
    task_category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT,
        help_text='Task/Issue Category',
    )
    task_description = models.TextField(blank=False, help_text='Description of the problem with this item')
    fix_description = models.TextField(blank=True, help_text='Description of actions taken to resolve the task')
    replacement_asset = models.ForeignKey(
        Assets,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text='Asset ID of item that was placed as a replacement',
        related_name='asset_replacement_task_ref',
    )
    management_comments = models.TextField(blank=True, help_text='Additional findings by management')
    state = models.ForeignKey(
        States,
        on_delete=models.PROTECT,
        help_text='Task state',
    )
    date_completed = models.DateTimeField(blank=True, null=True)
    resolved_by_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text='User that resolved this task',
        related_name='user_task_resolved_ref',
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{timestamp}-{asset}: {description}".format(
            timestamp=self.timestamp.strftime("%Y-%m-%d %H:%M"),
            asset=self.asset.number,
            description=self.task_description
        )

    class Meta:
        verbose_name = 'Repair Task'
        verbose_name_plural = 'Repair Tasks'

    @property
    def is_resolved(self):
        return self.state == States.objects.filter(state='Resolved').get()
    
    def clean(self):
        #if original state is resolved, don't allow update
        if self.pk is not None:
            resolved_state = States.objects.filter(state='Resolved').get()
            orig_task_instance = Tasks.objects.get(pk=self.pk)
            if orig_task_instance.state == resolved_state and self.state == resolved_state:
                raise ValidationError(
                    _("Invalid Update: Resolved tasks cannot be modified. Please change the resolution state\
                    to make any further changes."),
                    code='invalid',
                    params={},
                )
