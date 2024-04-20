from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post

from rest_framework import generics
from .serializers import PostSerializer
from .forms import PostForm

# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def all_posts(request):
    myposts = Post.objects.filter(show_in_api=True).values()
    template = loader.get_template('all_posts.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def post_details(request, post_id):
    mypost = Post.objects.filter(id=post_id, show_in_api=True).values().first()
    template = loader.get_template('post_details.html')
    context = {
        'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(show_in_api=True)
    serializer_class = PostSerializer

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(show_in_api=True)
    serializer_class = PostSerializer
    lookup_field = 'id'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts')  # Redirect to a page that shows all posts after successful creation
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts', post_id=post_id)  # Redirect to the detail page after successful edit
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})