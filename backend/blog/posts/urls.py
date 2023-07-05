from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post),
    path('post_list', views.post_list),
    path('post_nekaj', views.post_nekaj)
]