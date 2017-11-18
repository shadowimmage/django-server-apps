from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.db.models import F
from django.utils import timezone

# Models
from .models import *

# Forms
from .forms import KeySelectForm, CustomerEntryForm, CheckoutForm, ReturnForm, DueDateForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def index(request):
    # if incoming request is a POST - process the form data
    if request.method == 'POST':
        # generate a populated form with incoming data
        form = KeySelectForm(request.POST)
        # check whether the form data is valid
        if form.is_valid():
            # process the data in form.cleaned_data
            request.session['session_key_id'] = form.cleaned_data['key_lookup_id']
            # redirect to remainder of the process
            return redirect('keysApp:action')
        #form had a problem - return to the form page with params
        else:
            return render(request, 'keysApp/index.html', {'form': form})
    
    # if incoming request is a GET - return a blank form
    else:
        form = KeySelectForm()
    # send blank form for client to fill out.
    return render(request, 'keysApp/index.html', {'form': form})


# def index(request):
#     keyTypes_list = get_list_or_404(KeyTypes.objects.all())
#     return render(request, 'keysApp/index.html', {'keyTypes_list': keyTypes_list})

@require_http_methods(["GET", "POST"])
def action_page(request):
    # Get state of key based on records associated with the key,
    # Then, pass a dict of enabled to change the button state (enabled/disabled)
    # To allow only prescribed actions to be taken (Check out/Renew/Return)
    try:
        key = Keys.objects.get(pk=request.session['session_key_id'])
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')
    key_record_history = key.key_record_ref.order_by('date_out').reverse()
    most_recent_record_status = None
    if key_record_history.count() == 0:
        # key has never been checked out before.
        most_recent_record_status = 'Returned'
    else:
        # get the state of the most recent record - most up-to-date information
        most_recent_record_status = key_record_history[0].status
    #store information in a dictionary to be passed to the template
    key_info_dict = {'key': key, 'status': most_recent_record_status}
    # Copy safe strings to the session info for display purposes only - breaks data links
    request.session['key'] = str(key)
    request.session['key_status'] = str(most_recent_record_status)

    if most_recent_record_status == 'Checked out' or most_recent_record_status == 'Overdue':
        # Possible actions going forward: Renew, Return
        key_info_dict['checked_out'] = True
    elif most_recent_record_status == 'Returned':
        # Possible actions going forward: Check Out
        key_info_dict['checked_out'] = False

    # Possible actions that can be taken on a key - store in the session for action later.
    actions = ['checkout', 'renew', 'return']
    if request.method == 'POST':
        data = request.POST
        if data['action'] in actions:
            request.session['action'] = data['action']
            return redirect('keysApp:customer')

    return render(request, 'keysApp/action.html', {'key_info': key_info_dict, 'actions': actions})


@require_http_methods(["GET", "POST"])
def customer_info_page(request):
    # Prep page data from session data
    try:
        session_info_dict = {'key': request.session['key'], 'action': request.session['action']}
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')

    if request.method == 'POST':
        # Populate form with incoming data
        form = CustomerEntryForm(request.session, data=request.POST)
        # Check if the form is valid...
        if form.is_valid():
            # Pack up validated data into the session for confirmation at next step
            # Create an empty dictionary to start storing values:
            request.session['customer_info'] = {}
            for i, v in form.cleaned_data.items():
                if not isinstance(v, str):
                    request.session['customer_info'][i] = v.id
                else:
                    request.session['customer_info'][i] = v
            # Decide where to send the customer based on action selection previously
            if request.session['action'] == 'checkout':
                return redirect('keysApp:checkout')
            elif request.session['action'] == 'renew':
                return redirect('keysApp:renew')
            elif request.session['action'] == 'return':
                return redirect('keysApp:return')
        else:
            # Some problem with validation - return to page with submitted data
            return render(
                request,
                'keysApp/customer.html',
                {'session_info': session_info_dict, 'form': form}
            )
    else:
        # GET request - post blank form
        form = CustomerEntryForm(request.session)

    return render(
        request,
        'keysApp/customer.html',
        {'session_info': session_info_dict, 'form': form}
    )


@require_http_methods(["GET", "POST"])
def checkout_page(request):
    try:
        session_info_dict = {
            'key': request.session['key'],
            'customer': '{first} {last}'.format(
                first=request.session['customer_info']['form_first_name'],
                last=request.session['customer_info']['form_last_name']
            ),
            'action': request.session['action']
        }
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')
        # session_info_dict = {}

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # combine data from the session so far, and commit to the db
            key = Keys.objects.get(pk=request.session['session_key_id'])
            customer_query = Customers.objects.filter(
                email_address__iexact=request.session['customer_info']['form_email']
            )
            customer = None
            # if we have a matching customer in the database already, use that one.
            if customer_query.count() == 1:
                customer = customer_query.get()
            else:
                #  otherwise, we need to insert a new customer object
                customer = Customers(email_address = request.session['customer_info']['form_email'])
            customer.user_id = request.session['customer_info']['form_user_id']
            customer.last_name = request.session['customer_info']['form_last_name']
            customer.first_name = request.session['customer_info']['form_first_name']
            customer.phone_number = request.session['customer_info']['form_phone_number']
            customer.department = Departments.objects.get(
                pk=request.session['customer_info']['form_department']
            )
            customer.affiliation = Affiliations.objects.get(
                pk=request.session['customer_info']['form_affiliation']
            )
            record = Records(
                key=key,
                date_due=form.cleaned_data['form_due_date'],
                loan_term=form.cleaned_data['form_loan_term']
            )
            #Commit!!
            customer.save()
            # following ensures that if the customer was saved as an INSERT, customer has the given id.
            customer.refresh_from_db()
            record.customer=customer
            record.save()
            # if everything went well (and it should), put together the bits for the confirmation page
            request.session['customer_info']['customer_id'] = customer.id
            request.session['confirmation_type'] = "Due Date: "
            request.session['confirmation_detail'] = form.cleaned_data['form_due_date'].strftime("%x %X")
            return redirect('keysApp:confirmation')
    else:
        # GET request - give blank form
        form = CheckoutForm()
    
    return render(request, 'keysApp/checkout.html', {'session_info': session_info_dict, 'form': form})


@require_http_methods(["GET", "POST"])
def renew_page(request):
    try:
        session_info_dict = {
            'key': request.session['key'],
            'customer': '{first} {last}'.format(
                first=request.session['customer_info']['form_first_name'],
                last=request.session['customer_info']['form_last_name']
            ),
            'action': request.session['action']
        }
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')
        # session_info_dict = {}

    if request.method == 'POST':
        form = DueDateForm(request.POST)
        if form.is_valid():
            # combine data so far and commit the update to the db
            key = Keys.objects.get(pk=request.session['session_key_id'])
            customer_query = Customers.objects.filter(
                email_address__iexact=request.session['customer_info']['form_email']
            )
            customer = None
            # if we have a matching customer in the database already, use that one.
            if customer_query.count() == 1:
                customer = customer_query.get()
            else:
                #  otherwise, that's an error
                #TODO: need to have an info page for errors like this - index for now.
                return redirect('keysApp:index')
            # Update customer info
            customer.user_id = request.session['customer_info']['form_user_id']
            customer.last_name = request.session['customer_info']['form_last_name']
            customer.first_name = request.session['customer_info']['form_first_name']
            customer.phone_number = request.session['customer_info']['form_phone_number']
            customer.department = Departments.objects.get(
                pk=request.session['customer_info']['form_department']
            )
            customer.affiliation = Affiliations.objects.get(
                pk=request.session['customer_info']['form_affiliation']
            )

            # Update record info
            records = Records.objects.filter(
                customer=customer,
                key=key,
                is_returned=False,
            )
            record = records.get()
            record.extensions = F('extensions') + 1
            record.due_date = form.cleaned_data['form_due_date']
            #Commit!!
            customer.save()
            record.save()
            # if everything went well (and it should), put together the bits for the confirmation page
            request.session['customer_info']['customer_id'] = customer.id
            request.session['confirmation_type'] = "New Due Date: "
            request.session['confirmation_detail'] =  form.cleaned_data['form_due_date'].strftime("%x")
            return redirect('keysApp:confirmation')
    else:
        # GET request - give blank form
        form = DueDateForm()

    return render(request, 'keysApp/renew.html', {'session_info': session_info_dict, 'form': form})


@require_http_methods(["GET", "POST"])
def return_page(request):
    try:
        session_info_dict = {
            'key': request.session['key'],
            'customer': '{first} {last}'.format(
                first=request.session['customer_info']['form_first_name'],
                last=request.session['customer_info']['form_last_name']
            ),
            'action': request.session['action']
        }
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')
        # session_info_dict = {}

    if request.method == 'POST':
        data = request.POST
        if data['return'] == 'yes':
            key = Keys.objects.get(pk=request.session['session_key_id'])
            customer_query = Customers.objects.filter(
                email_address__iexact=request.session['customer_info']['form_email']
            )
            customer = None
            # if we have a matching customer in the database already, use that one.
            if customer_query.count() == 1:
                customer = customer_query.get()
            else:
                # This is an error, need to redirect to a error page.
                return redirect('keysApp:index')
            # Update customer info
            customer.user_id = request.session['customer_info']['form_user_id']
            customer.last_name = request.session['customer_info']['form_last_name']
            customer.first_name = request.session['customer_info']['form_first_name']
            customer.phone_number = request.session['customer_info']['form_phone_number']
            customer.department = Departments.objects.get(
                pk=request.session['customer_info']['form_department']
            )
            customer.affiliation = Affiliations.objects.get(
                pk=request.session['customer_info']['form_affiliation']
            )

            # Update record info
            records = Records.objects.filter(
                customer=customer,
                key=key,
                is_returned=False,
            )
            record = records.get()
            now = timezone.localtime()
            record.date_returned = now
            print(record.date_returned)
            #Commit!!
            customer.save()
            record.save()
            # if everything went well (and it should), put together the bits for the confirmation page
            request.session['customer_info']['customer_id'] = customer.id
            request.session['confirmation_type'] = "Key Returned at "
            request.session['confirmation_detail'] = now.strftime("%x %X")
            return redirect('keysApp:confirmation')
    return render(request, 'keysApp/return.html', {'session_info': session_info_dict})


@require_http_methods(["GET"])
def confirmation_page(request):
    try:
        session_info_dict = {
            'key': request.session['key'],
            'customer': '{first} {last}'.format(
                first=request.session['customer_info']['form_first_name'],
                last=request.session['customer_info']['form_last_name']
            ),
            'confirmation_type': request.session['confirmation_type'],
            'confirmation_detail': request.session['confirmation_detail']
        }
    except KeyError:
        # Session hasn't been set up properly - redirect to home page
        return redirect('keysApp:index')
        # session_info_dict = {}
    print(request.session['customer_info']['customer_id'])
    out_keys = Records.objects.filter(
        customer__id=request.session['customer_info']['customer_id'],
        is_returned=False
    )
    if out_keys.count() > 0:
        session_info_dict['out_keys'] = out_keys
    else:
        session_info_dict['out_keys'] = None
    #we're done with this info - clean things up.
    request.session.flush()
    return render(request, 'keysApp/confirmation.html', {'session_info': session_info_dict})