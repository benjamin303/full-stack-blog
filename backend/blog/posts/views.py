from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.

def main(request):
    template = loader.get_template('posts/main.html')
    return HttpResponse(template.render())

def posts(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('posts/all_posts.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mypost = Post.objects.get(id=id)
    template = loader.get_template('posts/details.html')
    context = {
        'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))

