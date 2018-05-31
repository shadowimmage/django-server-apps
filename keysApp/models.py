from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class KeyTypes(models.Model):
    key_type = models.CharField(db_index=True, max_length=32, unique=True,
        help_text='Key type code (usually stamped on key)')
    description = models.CharField(
        max_length=128,
        help_text='Description of this key type\'s function/use'
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Key Type'
        verbose_name_plural = 'Key Types'

    def __str__(self):
        return self.key_type


class Keys(models.Model):
    key_type = models.ForeignKey(
        KeyTypes,
        related_name='key_type_key_ref',
        on_delete=models.PROTECT,
        help_text='Type of key'
    )
    number = models.PositiveIntegerField(db_index=True,
        help_text='Serial number stamped on the physical key')
    # It might seem like this is redundant to store here, but it accelerates queries when a
    # customer is selecting a key to checkout/renew/return.
    # Whole batches of keys might also be retired due to disuse or other function as a business
    # operation outside of a record update.
    is_retired = models.BooleanField(db_index=True, default=False,
        help_text="Flag key as retired for loss, destroyed, etc.")
    RETIREMENT_CHOICES = (
        (None, 'N/A'),
        (1, 'Lost'),
        (2, 'Disposed')
    )
    retirement_type = models.PositiveSmallIntegerField(
        db_index=True,
        choices=RETIREMENT_CHOICES,
        default=None,
        blank=True,
        null=True,
        help_text="Type of retirement - required if retired = true."
    )
    retirement_comment = models.TextField(default='', blank=True,
        help_text="Detail why key has been flagged as retired"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Key'
        verbose_name_plural = 'Keys'
        unique_together = (('key_type', 'number'),)

    @property
    def is_returned(self):
        if self.checked_out_lost_count > 0:
            return False
        else:
            return True

    @property
    def checked_out_lost_count(self):
        return self.key_record_ref.all().filter(is_returned=False).count()

    @property
    def lost_record_count(self):
        return self.key_record_ref.all().filter(is_lost_broken=True).count()

    def __str__(self):
        return "{0} {1}".format(self.key_type, self.number)

    def clean(self):
        # Don't allow retirement type or comment to be empty/without data if is_retured = True
        if self.is_retired == True:
            if self.retirement_type == None or self.retirement_comment == '':
                raise ValidationError(
                    _("Invalid Update: retirement comment and type are required if key is retired."),
                    code='invalid',
                    params={},
                )
            # Don't allow retirement if there are outstanding Records that are not returned or lost.
            if self.checked_out_lost_count > 0 or self.lost_record_count > 0:
                raise ValidationError(
                    _("Invalid Update: Key cannot be retired until all associated checkout records\
                    have been flagged as returned or lost."),
                    code='invalid',
                    params={},
                )
        # If the retirement flag is cleared, be sure that the other associated fields are cleared too.
        if self.is_retired == False:
            if self.retirement_type != None or self.retirement_comment != '':
                raise ValidationError(
                    _("Invalid Update: if un-retiring this key, please clear other retirement\
                    fields as well."),
                    code='invalid',
                    params={},
                )


class LoanTerms(models.Model):
    term_desc = models.CharField(max_length=64, unique=True)
    term_length = models.PositiveSmallIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Loan Term'
        verbose_name_plural = 'Loan Terms'
        unique_together = (('term_desc', 'term_length'),)

    def __str__(self):
        return "{description}".format(
            description=self.term_desc
            )


class Affiliations(models.Model):
    affiliation = models.CharField(max_length=64, unique=True)
    customer_user_id_reqd = models.BooleanField(default=True,
        help_text="set if a customer with this kind of affiliation needs to provide a user id.")
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Affiliation'
        verbose_name_plural = 'Affiliations'

    def __str__(self):
        return self.affiliation


class Departments(models.Model):
    dept_name = models.CharField(max_length=64, unique=True)
    box_number = models.PositiveIntegerField()
    admin_name = models.CharField(max_length=64, blank=True)
    admin_contact = models.CharField(max_length=64, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.dept_name


class Customers(models.Model):
    user_id = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(db_index=True, max_length=64)
    first_name = models.CharField(db_index=True, max_length=64)
    phone_number = models.CharField(max_length=64)
    email_address = models.EmailField(unique=True)
    email_is_bad = models.BooleanField(default=False)
    department = models.ForeignKey(
        Departments,
        related_name='department_cust_ref',
        on_delete=models.PROTECT
    )
    affiliation = models.ForeignKey(
        Affiliations,
        related_name='affiliation_cust_ref',
        on_delete=models.PROTECT
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "{0}, {1}, {2}".format(self.last_name, self.first_name, self.user_id)

def default_due_time():
    now = timezone.localtime()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

class Records(models.Model):
    customer = models.ForeignKey(
        Customers,
        related_name='customer_record_ref',
        on_delete=models.PROTECT
    )
    key = models.ForeignKey(
        Keys,
        related_name='key_record_ref',
        on_delete=models.PROTECT
    )
    date_out = models.DateTimeField(db_index=True, default=timezone.localtime)
    date_due = models.DateTimeField(db_index=True, default=default_due_time)
    loan_term = models.ForeignKey(
        LoanTerms,
        related_name='loan_term_record_ref',
        null=True,
        on_delete=models.SET_NULL
    )
    extensions = models.PositiveSmallIntegerField(default=0)
    date_returned = models.DateTimeField(blank=True, null=True)
    is_returned = models.BooleanField(db_index=True, default=False)
    is_overdue = models.BooleanField(db_index=True, default=False)
    number_reminders_sent = models.PositiveSmallIntegerField(default=0)
    date_email_reminder_sent = models.DateTimeField(blank=True, null=True)
    is_lost_broken = models.BooleanField(db_index=True, default=False)
    date_paid_for = models.DateField(blank=True, null=True,
        help_text='Note the date that customer paid for loss/destruction/etc. of key.')
    payment_notes = models.TextField(default='', blank=True,
        help_text='Notes regarding payment, including EMS# and Connect REQ#, if applicable.')
    admin_comment = models.TextField(default='', blank=True,
        help_text='Notes about this key record. Include special circumstances and\
        information regarding associated Connect records.')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        unique_together = (('customer', 'key', 'date_out', 'is_returned', 'is_overdue'))

    @property
    def status(self):
        "Returns the status of this record, ie. 'Checked Out', 'Overdue', 'Returned', 'Lost', etc."
        if self.is_returned:
            return "Returned"
        elif self.date_paid_for is not None:
            return "Paid"
        elif self.is_lost_broken:
            return "Lost/Broken"
        elif self.is_overdue:
            return "Overdue"
        elif not self.is_overdue:
            return "Checked out"

    def __str__(self):
        return "{0}, {1}, {2}".format(self.customer, self.key, self.date_out)

    # Override built-in clean method to implement model-level validation.
    def clean(self):
        # disallow a key to be associated with more than one concurrent checkout record
        # at a time without all others being 'returned'
        if self.key.checked_out_lost_count > 0:
            # make sure its not this record (update case)
            if self.key.key_record_ref.all().filter(is_returned=False).count() > 1:
                raise ValidationError(
                    _('Key %(key)s is already checked out to someone else.')
                )
        # disallow the return date to be before the checkout date.
        if self.date_returned is not None:
            if (self.date_returned - self.date_out).total_seconds() < 0:
                raise ValidationError(
                    _('Return date (%(return)s) cannot be before Checkout date (%(out)s).'),
                    code='invalid',
                    params={
                        'return': self.date_returned.strftime('%x %X'),
                        'out': self.date_out.strftime('%x %X'),
                    }
                )
        # disallow the due date to be before the checkout date.
        if (self.date_due - self.date_out).total_seconds() < 0:
            raise ValidationError(
                _('Due date (%(due)s) cannot be before checkout date (%(out)s).'),
                code='invalid',
                params={
                    'due': self.date_due.strftime('%x %X'),
                    'out': self.date_out.strftime('%x %X'),
                }
            )
        # disallow keys to be both lost/broken and returned at the same time.
        if self.is_returned and self.is_lost_broken:
            raise ValidationError(
                _('Records cannot reflect a key being both lost/broken and returned.')
            )
        # If payment has been made, require there to be notes.
        if self.date_paid_for is not None and self.payment_notes == '':
            raise ValidationError(
                _('Notes about payment must be entered if payment has been made. Include EMS\
                or Connect record numbers.')
            )
        # If payment date is cleared, require payment notes to follow.
        if self.date_paid_for is None and self.payment_notes != '':
            raise ValidationError(
                _('If payment date has been cleared, payment notes must be cleared as well.\
                If necessary, copy notes to Admin Comments.')
            )
        # if key was found, and thus the lost flag has been cleared, require payment details
        # to be cleared as well.
        if self.is_lost_broken == False:
            if self.date_paid_for is not None or self.payment_notes != '':
                raise ValidationError(
                    _('If Lost/Broken is false, payment date and payment notes must be cleared.\
                    If necessary, place additional notes in Admin Comments.')
                )

    # Override the built in save function to run any state-change or other calculations
    # based on information that will change on update or save.
    def save(self, *args, **kwargs):
        self.status_update()
        super(Records, self).save(*args, **kwargs)

    # Updates the Status of the key Record based on flags and dates entered on the record.
    def status_update(self):
        "Updates is_overdue and is_returned based on dates"
        # get current time
        now = timezone.localtime()

        # update is_overdue
        # time difference (delta) is negative if the due date has passed.
        out_due_delta = self.date_due - now
        out_due_delta_secs = out_due_delta.total_seconds()
        if out_due_delta_secs <= 0:
            # due date has passed.
            self.is_overdue = True
        else:
            self.is_overdue = False

        # Update is_returned
        if self.date_returned is not None:
            self.is_returned = True
        else:
            self.is_returned = False



class LoanExceptions(models.Model):
    customer = models.ForeignKey(
        Customers,
        related_name='customer_loanExceptions_ref',
        on_delete=models.CASCADE,
        help_text='Customer that this loan exception applies to'
    )
    key_type = models.ForeignKey(
        KeyTypes,
        related_name='key_type_loanExceptions_ref',
        on_delete=models.CASCADE,
        help_text='Type of key the customer is allowed a loan exception of'
    )
    date_expires = models.DateField(
        help_text='Date that this exception will expire'
    )
    limit = models.PositiveSmallIntegerField(
        default=2,
        help_text='Limit the number of concurrent check outs by this customer of this key type'
    )
    granted_by = models.CharField(
        db_index=True,
        max_length=128
    )
    admin_comment = models.TextField(default='', blank=True,
        help_text='Notes about this loan exception. Include special circumstances and\
        information, including associated Connect records.'
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Loan Exception'
        verbose_name_plural = 'Loan Exceptions'

    @property
    def is_expired(self):
        "Returns a boolean based on whether the expiration date for the loan exception has passed."
        return (self.date_expires - date.today()).total_seconds() < 0

    def __str__(self):
        return "Customer: {customer}; type: {type}; limit: {limit}".format(
            customer=self.customer,
            type=self.key_type,
            limit=self.limit
        ) 

    def clean(self):
        # Exceptions must expire in the future.
        if (self.date_expires - date.today()).total_seconds() < 0:
            raise ValidationError(
                _('Expiration date (%(date)s) cannot be before today\'s date (%(today)s).'),
                code='invalid',
                params={
                    'date': str(self.date_expires),
                    'today': str(date.today()),
                }
            )

