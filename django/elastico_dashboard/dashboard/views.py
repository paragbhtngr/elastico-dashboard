from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hayyyy ;D')

def buyer(request):
    template = loader.get_template('dashboard/buyer-content.html')
    return HttpResponse(template.render(request))

def seller(request):
    template = loader.get_template('dashboard/seller-content.html')
    return HttpResponse(template.render(request))
