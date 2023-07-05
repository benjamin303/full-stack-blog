# from django.urls import path
# from posts import views

# urlpatterns = [
#     path('', views.main),
#     path('posts/', views.posts),
#     path('posts/details/<int:id>', views.details)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('posts', views.posts, name='posts'),
    path('posts/details/<int:id>', views.details, name='post_details'),
]