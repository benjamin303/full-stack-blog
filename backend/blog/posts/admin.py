# from django.contrib import admin
# from .models import Post

# # Register your models here.

# admin.site.register(Post)

from django.contrib import admin
from .models import Post, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass