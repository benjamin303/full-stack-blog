from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    featured_image = serializers.SerializerMethodField()

    def get_featured_image(self, obj):
        if obj.featured_image:
            # Assuming the 'MEDIA_URL' is properly configured in your Django settings
            return self.context['request'].build_absolute_uri(obj.featured_image.url)
        return None

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'featured_image']  # Include the fields you want to serialize
