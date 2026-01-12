from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def cart_home(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def cart_details(request):
    return HttpResponse("Hello Word")