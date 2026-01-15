from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def cart_home(request):
    member = Member.objects.all().values()
    print(member[0])
    print(type(member[0]))
    template = loader.get_template('all_members.html')
    context = {
        'members' : member
    }
    return HttpResponse(template.render(context,request)) # We have to pass dictionary

def cart_details(request,id):
    # breakpoint(id)
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : member
    }
    return HttpResponse(template.render(context,request))