from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user(request):
    return HttpResponse("this is USER of my new site")

def user_list(request):
    return HttpResponse("ths is USER LIST")

def user_test(request):
    return HttpResponse("this is USER TEST")
