from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def index(request):
    context = {
        'meta_description': 'This is the meta description',
        'page_name': 'dashboard'
    }
    return render(request, 'dashboard/index.html', context)

def login(request):
    context = {
        'meta_description': 'This is the meta description',
        'page_name': 'login'
    }
    return render(request, 'dashboard/login.html', context)
