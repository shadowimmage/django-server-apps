from django.contrib import admin

# Register your models here.
from . import models

class KeyTypesAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added')
    fieldsets = [
        ('Types', {'fields': ['key_type', 'description']}),
        ('Dates', {'fields': ['date_updated', 'date_added']}),
    ]
    list_display = ('key_type', 'description', 'date_updated')
    search_fields = ('key_type',)

admin.site.register(models.KeyTypes, KeyTypesAdmin)

class KeysAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added',)
    fieldsets = [
        ('Key', {'fields': ['key_type', 'number']}),
        ('Retirement',
            {'fields': ['is_retired', 'retirement_type', 'retirement_comment'],
            'classes': ['collapse']}
        ),
        ('Dates', {'fields': ['date_added', 'date_updated']})
    ]
    list_display = ('key_type', 'number', 'is_returned', 'is_retired', 'date_updated')
    list_filter = ('is_retired',)
    search_fields = ('key_type', 'number',)

admin.site.register(models.Keys, KeysAdmin)

class LoanTermsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added')
    fields = ['term_desc', 'term_length', 'date_updated', 'date_added']
    list_display = ('term_desc', 'term_length', 'date_updated')

admin.site.register(models.LoanTerms, LoanTermsAdmin)

class AffiliationsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added',)
    fields = ['affiliation', 'customer_user_id_reqd', 'date_updated', 'date_added']
    list_display = ('affiliation', 'customer_user_id_reqd', 'date_updated')

admin.site.register(models.Affiliations, AffiliationsAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_updated')
    fields = ['dept_name', 'box_number', 'admin_name', 'admin_contact', 'date_updated', 'date_added']
    list_display = ('dept_name', 'box_number', 'admin_name', 'admin_contact')

admin.site.register(models.Departments, DepartmentsAdmin)

class CustomersAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added')
    fieldsets = [
        ('Customer', {'fields': [('user_id', 'last_name', 'first_name'), 'affiliation']}),
        ('Contact info', {'fields': ['phone_number', 'email_address', 'department']}),
        ('Dates', {'fields': ['date_updated', 'date_added'], 'classes': ['collapse']}),
    ]
    list_display = ('user_id', 'last_name', 'first_name', 'email_address', 'affiliation', 'department')

admin.site.register(models.Customers, CustomersAdmin)

class RecordsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added', 'extensions', 'is_returned', 'is_overdue')
    fieldsets = [
        ('Customer', {'fields': ['customer']}),
        ('Key', {'fields': ['key']}),
        ('Dates', {'fields': [('date_out', 'date_due', 'loan_term')]}),
        ('Status',{'fields': [('is_returned', 'date_returned'), 'is_overdue', 'extensions']}),
        ('Loss',
            {'fields': [('is_lost_broken', 'date_paid_for'), 'payment_notes'],
            'classes': ['collapse']}
        ),
        ('Reminders',
            {'fields': [('date_email_reminder_sent', 'number_reminders_sent')],
            'classes': ['collapse']}
        ),
        ('Admin Comments', {'fields': ['admin_comment']}),
        ('Record Dates', {'fields': [('date_added', 'date_updated')], 'classes': ['collapse']}),
    ]
    list_display = (
        'customer',
        'key',
        'status',
        'date_out',
        'date_due',
        'is_returned',
        'is_overdue',
        'is_lost_broken'
    )
    list_filter = ('is_returned', 'is_overdue', 'is_lost_broken')
    search_fields = (
        'key__key_type__key_type',
        'key__number',
        'customer__user_id',
        'customer__first_name',
        'customer__last_name',
    )

admin.site.register(models.Records, RecordsAdmin)


class LoanExceptionsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated', 'date_added',)
    fieldsets = [
        ('Customer', {'fields': ['customer']}),
        ('Exception', {'fields': [('key_type', 'limit', 'date_expires')]}),
        ('Administrative Details', {'fields': ['granted_by', 'admin_comment']}),
        ('Record Dates', {'fields': [('date_added', 'date_updated')], 'classes': ['collapse']}),
    ]
    list_display = (
        'customer',
        'key_type',
        'limit',
        'is_expired',
        'granted_by',
        'date_updated',
    )
    list_filter = ('key_type', 'date_expires')
    search_fields = (
        'key_type__key_type',
        'customer__user_id',
        'customer__first_name',
        'customer__last_name',
        'granted_by',
    )

admin.site.register(models.LoanExceptions, LoanExceptionsAdmin)