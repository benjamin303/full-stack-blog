# from django.db import models
# # from django.contrib.auth import get_user_model

# # User = get_user_model()

# # Create your models here.

# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     slug = models.SlugField(unique=True)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateField(auto_now_add=True)
#     published_date = models.DateField(null=True, blank=True)
#     keywords = models.CharField(max_length=255, blank=True)
#     show_in_api = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.title} {self.created_date}"


# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
#     image = models.ImageField(upload_to='post_images/')

#     def __str__(self):
#         return f"Photo for Post: {self.post.title}"


from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(null=True, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    show_in_api = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.created_date}"

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Photo for Post: {self.post.title}"