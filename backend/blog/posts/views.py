from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def all_posts(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('all_posts.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def post_details(request, post_id):
    mypost = Post.objects.get(id=post_id)
    template = loader.get_template('post_details.html')
    context = {
        'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'