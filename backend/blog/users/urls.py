from django.urls import path
from users import views

urlpatterns = [
    path('', views.user),
    path('user_list', views.user_list),
    path('user_test', views.user_test),
]