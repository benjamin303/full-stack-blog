from django.urls import path
from . import views

app_name = 'posts'

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('posts/', views.posts, name='posts'),
#     path('posts/details/<int:id>', views.details, name='details'),
# ]

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('details/<int:post_id>/', views.post_details, name='post_details'),
]