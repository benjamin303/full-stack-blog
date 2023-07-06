# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from .models import Post
# from .serializers import PostSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# # Create your views here.

# def main(request):
#     template = loader.get_template('posts/main.html')
#     return HttpResponse(template.render())

# # def posts(request):
# #     myposts = Post.objects.all().values()
# #     template = loader.get_template('posts/all_posts.html')
# #     context = {
# #         'myposts': myposts,
# #     }
# #     return HttpResponse(template.render(context, request))

# # def posts(request):
# #     myposts = Post.objects.all()
# #     serializer = PostSerializer(myposts, many=True)  # Serialize multiple objects
# #     return Response(serializer.data)

# @api_view(['GET'])
# def posts(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)

# posts.get_queryset = lambda: Post.objects.all()  # Add this line to define the get_queryset method

# def details(request, id):
#     mypost = Post.objects.get(id=id)
#     template = loader.get_template('posts/details.html')
#     context = {
#         'mypost': mypost,
#     }
#     return HttpResponse(template.render(context, request))


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

def main(request):
    template = loader.get_template('posts/main.html')
    return HttpResponse(template.render())

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def posts(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

# Add the get_queryset method to the view
posts.get_queryset = lambda: Post.objects.all()

def details(request, id):
    mypost = Post.objects.get(id=id)
    template = loader.get_template('posts/details.html')
    context = {
        'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))
