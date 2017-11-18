from django.contrib import admin

# Register your models here.
from . import models

class MakersAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('Manufacturer', {'fields': ['maker']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['maker', 'date_updated']
    list_filter = ['maker']
    search_fields = ('maker',)

admin.site.register(models.Makers, MakersAdmin)

class MakeModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('Model', {'fields': ['make', 'model_name', 'description']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['make', 'model_name']
    list_filter = ['make']
    search_fields = ['make', 'model_name']

admin.site.register(models.MakeModel, MakeModelAdmin)

class AssetsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('Asset', {'fields': ['number', 'model', 'serial', 'description', 'mac_address', 'notes']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['number', 'model', 'serial', 'mac_address', 'date_updated']
    list_filter = ['model']
    search_fields = ['number', 'model', 'serial', 'mac_address',]

admin.site.register(models.Assets, AssetsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('Category', {'fields': ['category', 'description']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['category', 'date_updated']
    search_fields = ['category']

admin.site.register(models.Categories, CategoriesAdmin)

class StatesAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('State', {'fields': ['state', 'description']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['state', 'description', 'date_updated']
    search_fields = ['state']

admin.site.register(models.States, StatesAdmin)

class ComponentsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created')
    fieldsets = [
        ('Component', {'fields': ['model', 'serial', 'notes']}),
        ('Dates', {'fields': ['date_updated', 'date_created']}),
    ]
    list_display = ['model', 'serial', 'date_created']
    list_filter = ['model',]
    search_fields = ['model', 'serial',]

admin.site.register(models.Components, ComponentsAdmin)

class AssetComponentAssemblyAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_created',)
    fieldsets = [
        ('Assembly', {'fields': ['asset', 'component',]}),
        ('Dates', {'fields': ['date_updated', 'date_created',]}),
    ]
    list_display = ['asset', 'component', 'date_updated',]
    list_filter = ['date_updated']
    search_fields = ['asset', 'component',]

admin.site.register(models.AssetComponentAssembly, AssetComponentAssemblyAdmin)

class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', 'date_updated', 'date_created')
    fieldsets = [
        ('Summary', {'fields': ['asset', 'task_description', 'submitted_by_user', 'state']}),
        ('Detail', {'fields': ['task_date', 'task_category', 'original_location', 'replacement_asset']}),
        ('Fix', {'fields': ['fix_description', 'management_comments', 'date_completed', 'resolved_by_user']}),
        ('Dates', {'fields': ['timestamp', 'date_updated', 'date_created',]}),
    ]
    list_display = ['asset', 'task_date', 'task_category', 'task_description', 'state', 'original_location']
    list_filter = ['state', 'task_date', 'task_category', 'submitted_by_user', 'resolved_by_user']
    search_fields = ['asset', 'replacement_asset', 'original_location', 'task_description', 'submitted_by_user', 'resolved_by_user']

admin.site.register(models.Tasks, TasksAdmin)
