from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # A slug field for URL-friendly representation of the title
    # author = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model for authors
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    # categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title} {self.created_date}"