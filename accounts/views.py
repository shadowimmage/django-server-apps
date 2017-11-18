from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user.get_username})

# def login_fail(request):
#     return render(request, 'accounts/loginfail.html')

def error_page(request):
    return render(request, 'accounts/error_page.html')