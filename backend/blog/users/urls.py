from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('details/<int:user_id>/', views.user_details, name='user_details'),
    path('create/', views.create_user, name='create_user'),
    path('user/<int:user_id>/edit/', views.edit_user, name='edit_user'),
]