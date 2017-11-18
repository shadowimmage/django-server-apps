# from django.forms import ModelForm
# from .models import Keys
# from django.utils.translation import ugettext_lazy as _

# class KeySelectForm(ModelForm):
#     class Meta:
#         model = Keys
#         fields = ['key_type', 'number']

from django import forms
from .models import Keys, KeyTypes, Departments, Affiliations, Customers, LoanExceptions, LoanTerms
from django.forms import ModelChoiceField, IntegerField, CharField, EmailField, DateTimeField
# validation supoort
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime, timedelta, time
from django.utils import timezone

# Subclass the default behavior to include the description in the selection menu
class KeyTypeChoiceField(ModelChoiceField):
    #override normal text display method
    def label_from_instance(self, obj):
        return "{0} - {1}".format(obj.key_type, obj.description)

class KeySelectForm(forms.Form):
    form_keyType = KeyTypeChoiceField(
        widget=forms.Select(
            attrs=
            {'class': 'form-control'}
        ),
        queryset=KeyTypes.objects.all(),
        label='Key Type',
        empty_label='select type'
    )

    form_keyNum = IntegerField(
        widget=forms.NumberInput(
            attrs=
            {'class': 'form-control',
            'placeholder': 'eg. 1234'}
        ),
        label='Number',
        min_value=0,
        max_value=9999
    )

    # TODO: put in logic to disallow key from being selected if it is lost or paid for - redirecting them for staff assistance.
    def clean(self):
        cleaned_data = super(KeySelectForm, self).clean()
        cd_type = cleaned_data.get('form_keyType')
        cd_number = cleaned_data.get('form_keyNum')
        if cd_type and cd_number:
            if Keys.objects.filter(key_type_id=cd_type, number=cd_number).count() == 1:
                #found the key in the database.
                key_id = Keys.objects.get(key_type_id=cd_type, number=cd_number).id
                # Ensure key being checked out is not 'retired'
                if Keys.objects.get(pk=key_id).is_retired:
                    raise forms.ValidationError(
                        _('Invalid key selection: \"%(type)s %(num)s\" is retired.'),
                        code='invalid',
                        params={'type': cd_type, 'num': cd_number},
                    )
                    # replace the cleaned data with the key ID
                return {'key_lookup_id': key_id}
            else:
                raise forms.ValidationError(
                    _('Invalid Key Lookup: \"%(type)s %(num)s\" not found in database.'),
                    code='invalid',
                    params={'type': cd_type, 'num': cd_number},
                )
        else:
            raise forms.ValidationError(
                _('Form error: type/number invalid (%(type)s %(num)s)'),
                code='error',
                params={'type': cd_type, 'num': cd_number},
            )


class CustomerEntryForm(forms.Form):
    # allow access to session data for form validation
    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(CustomerEntryForm, self).__init__(*args, **kwargs)

    # Affiliation
    form_affiliation = ModelChoiceField(
        widget=forms.Select(
            attrs=
            {'class': 'form-control'}
        ),
        queryset=Affiliations.objects.all(),
        label='Affiliation',
        empty_label='Select UW affiliation'
    )
    # Customer personal info
    form_user_id = CharField(
        widget=forms.TextInput(
            attrs=
            {'class': 'form-control',
            'placeholder': 'User ID'}
        ),
        label='User ID',
        max_length=8,
        required=False,
    )
    form_first_name = CharField(
        widget=forms.TextInput(
            attrs=
            {'class': 'form-control',
            'placeholder': 'First'}
        ),
        label='First Name',
    )
    form_last_name = CharField(
        widget=forms.TextInput(
            attrs=
            {'class': 'form-control',
            'placeholder': 'Last'}
        ),
        label='Last Name',
    )
    # Contact info
    form_phone_number = CharField(
        widget=forms.TextInput(
            attrs=
            {'class': 'form-control',
            'placeholder': '206-221-5000'}
        ),
        label='Phone Number'
    )
    form_email = EmailField(
        widget=forms.EmailInput(
            attrs=
            {'class': 'form-control',
            'placeholder': 'dubs@uw.edu'}
        ),
        label='Email Address',
        help_text='<span class="glyphicon glyphicon-warning-sign"></span>\
            Do not use departmental or shared email addresses.'
    )
    form_department = ModelChoiceField(
        widget=forms.Select(
            attrs=
            {'class': 'form-control'}
        ),
        queryset=Departments.objects.all(),
        label='Department',
        empty_label='Select UW department or Other'
    )

    # Validates customer entry
    def clean(self):
        cleaned_data = super(CustomerEntryForm, self).clean()
        cd_affiliation = cleaned_data.get('form_affiliation')
        cd_netid = cleaned_data.get('form_user_id')
        if cd_affiliation:
            if cd_affiliation.customer_user_id_reqd:
                if not cd_netid or cd_netid == '':
                    raise forms.ValidationError(
                        _('Invalid entry: \"%(affiliation)s\" affiliation requires NetID to be entered.'),
                        code='invalid',
                        params={'affiliation': str(cd_affiliation)}
                    )
        # Check if this customer can check out this kind of key:
        # If customer email already in system...
        customer_query = Customers.objects.filter(email_address__iexact=cleaned_data.get('form_email'))
        if customer_query.count() == 1:
            customer = customer_query.get()
            # Check if they already have one of these key types
            transaction_key = Keys.objects.get(pk=self.session['session_key_id'])
            # get the number of unreturned key records associated with this customer
            unreturned_keys = customer.customer_record_ref.filter(is_returned=False)
            unreturned_type_match_count = unreturned_keys.filter(key__key_type=transaction_key.key_type).count()
            # This only applies if the customer is making a new checkout.
            if unreturned_type_match_count > 0 and self.session['action'] == 'checkout':
                # does this customer have an exception to allow checkout of more than 1 of this key?
                customer_loan_exception_exists = LoanExceptions.objects.filter(
                    customer=customer,
                    key_type=transaction_key.key_type,
                    date_expires__gt=date.today(),
                    limit__gt=unreturned_type_match_count
                ).exists()
                if not customer_loan_exception_exists:
                    # Customer does not have sufficient permissions to allow additional key checkout of this type.
                    raise forms.ValidationError(
                        _('Error: Customers cannot check out more than 1 of any key type without an exception,\
                        please see staff for assistance.'),
                        code='error',
                        params={},
                    )
                else:
                    # Customer has an exception to allow this checkout, and will not go over the exception limit.
                    # OR they are renewing/returning.
                    pass
            else:
                #customer may have overdue keys of another type!
                #TODO care about that later.
                pass
        else:
            #customer does not exist in the system
            # is this a new checkout? If not, then the customer must be in the system.
            if self.session['action'] != 'checkout':
                raise forms.ValidationError(
                    _('Keys can only be renewed or returned by the person who checked them out.\
                    Please check the email address entered.\
                    If you continue to experience difficulties,\
                    please see staff for assistance.'),
                    code='error',
                    params={},
                )
            pass


class DueDateForm(forms.Form):
    form_due_date = DateTimeField(
        widget=forms.DateTimeInput(
            attrs=
            {'id': 'datepicker',
            'class': 'form-control',
            'placeholder': 'Select Date'}),
        label='Due Date'
    )

    def clean_form_due_date(self):
        cd_date = self.cleaned_data.get('form_due_date')
        # create a timezone-aware timestamp, with no microsecond precision
        now = timezone.now().astimezone().replace(microsecond=0)
        # add the current time to the date
        cd_datetime = cd_date.replace(hour=now.hour, minute=now.minute, second=now.second)
        # Due date must be in the future
        if (cd_datetime - now).total_seconds() < 0:
            raise forms.ValidationError(
                _('Invalid entry: Due Date must be in the future'),
                code='invalid',
                params={},
            )
        else:
            # return modified date in cleaned_data with the converted datetime.
            return cd_datetime


class CheckoutForm(DueDateForm):
    form_loan_term = ModelChoiceField(
        widget=forms.Select(
            attrs=
            {'class': 'form-control'}
        ),
        queryset=LoanTerms.objects.all(),
        label='Loan Term',
        empty_label='select duration'
    )


class ReturnForm(forms.Form):
    pass

""" sample validation stuff
raise forms.ValidationError(
    _('Invalid value: %(value)s'),
    code='invalid',
    params={'value': '42'},
)"""



'''
date input
https://www.w3schools.com/html/html_form_input_types.asp
'''