from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='user_details'),
    path('testing', views.user_test, name='user_test'),
]
