from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def cart_home(request):
    member = Member.objects.all().values()
    print(member[0]['id'])
    print(type(member[0]))
    template = loader.get_template('first.html')
    return HttpResponse(template.render(member[0],request)) # We have to pass dictionary

def cart_details(request):
    return HttpResponse("Hello Word")