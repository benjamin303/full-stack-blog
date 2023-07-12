from django.urls import path
from . import views

app_name = 'users'

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('users/', views.users, name='users'),
#     path('users/details/<int:id>', views.details, name='details'),
# ]

# urlpatterns = [
#     path('', views.main, name='user-main'),
#     path('users/', views.users, name='users-list'),
#     path('users/details/<int:id>', views.details, name='user-detail'),
# ]

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('details/<int:user_id>/', views.user_details, name='user_details'),
]