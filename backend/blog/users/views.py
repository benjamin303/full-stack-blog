from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User

from rest_framework import generics
from .serializers import UserSerializer
from .forms import UserForm

# Create your views here.

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

def create_user(request):
    print("Inside create_user view")
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/users')  # Redirect to a page that shows all posts after successful creation
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def edit_user(request, user_id):
    print("Inside edit_user view")
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/users', user_id=user_id)  # Redirect to the detail page after successful edit
    else:
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form})