from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'meta_description': 'This is the meta description',
        'page_name': 'dashboard'
    }
    return render(request, 'dashboard/index.html', context)
