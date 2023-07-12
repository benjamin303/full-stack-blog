from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.

# def users(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def all_users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def user_details(request, user_id):
    myuser = User.objects.get(id=user_id)
    template = loader.get_template('user_details.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))
