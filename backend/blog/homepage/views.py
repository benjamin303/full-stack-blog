from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is HOMEPAGE of my new site")

def signup(request):
    return HttpResponse("please SIGNUP to receive our news")

def login(request):
    return HttpResponse("already a member ! please LOGIN")
