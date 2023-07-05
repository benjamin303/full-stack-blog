from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post(request):
    return HttpResponse("this is the POST homepage")

def post_list(request):
    return HttpResponse("this is the list POST LIST")

def post_nekaj(request):
    return HttpResponse("this is POST NEKAJ")
