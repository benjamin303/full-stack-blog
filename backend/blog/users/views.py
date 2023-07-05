from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.

def main(request):
    template = loader.get_template('users/main.html')
    return HttpResponse(template.render())

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('users/all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myuser = User.objects.get(id=id)
    template = loader.get_template('users/details.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))

def user_test(request):
    return HttpResponse("this is USER TEST")
