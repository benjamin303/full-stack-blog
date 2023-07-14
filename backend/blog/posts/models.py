from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(null=True, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    images = models.ImageField(upload_to='post_images/', null=True, blank=True)

    show_in_api = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.created_date}"