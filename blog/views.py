from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serialization import PostSerializer
from rest_framework import status
from rest_framework import serializers 
# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls= {
        'allblogs': '/',
        'addedblog': '/create',
        'update': '/update/pk',
    }
    return Response(api_urls)
@api_view(['POST'])
def Add_blog(request):
    blog= PostSerializer(data= request.data)
    # Validating for already existing data
    if Post.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists.')
    if blog.is_valid():
        blog.save()
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def view_blogs(request):
    if request.query_params:
        blogs= Post.objects.filter(**request.query_params.dict())
    else:
        blogs= Post.objects.all()

    if blogs:
        serializers= PostSerializer(blogs,many=True)
        return Response(serializers.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_blog(request,pk):
    blog= Post.objects.get(pk=pk)
    data= PostSerializer(instance= blog, data= request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    
