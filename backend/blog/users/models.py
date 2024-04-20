from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):

    def user_profile_picture_path(instance, filename):
        return f'user_profiles/{filename}'

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='user_profiles', null=True, blank=True)
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, null=True, blank=True)
    joined_date = models.DateField(null=True, default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    gender = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=1, choices=gender, default="M", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

