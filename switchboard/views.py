from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'switchboard/index.html')