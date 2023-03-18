from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['GET'])
def listAllBlogs(request):
    blogs = Blog.objects.order_by('date_created')
    blogsSerializer = BlogSerializer(blogs, many=True)
    return Response(blogsSerializer.data)

@api_view(['GET'])
def listThreeBlogs(request):
    blogs = Blog.objects.order_by('date_created')
    blogsSerializer = BlogSerializer(blogs[:3], many=True)
    return Response(blogsSerializer.data)

@api_view(['GET'])
def getBlog(request, blogID):
    blog = Blog.objects.get(id=blogID)
    blogSerializer = BlogSerializer(blog, many=False)
    return Response(blogSerializer.data)


@api_view(['GET'])
def searchBlogs(request, searchQuery):
    blogs = Blog.objects.all()
    searchResults = []
    for blog in blogs:
        if searchQuery in blog.content or searchQuery in blog.title:
            searchResults.append(blog)
    blogSerializer = BlogSerializer(searchResults, many=True)
    return Response(blogSerializer.data)