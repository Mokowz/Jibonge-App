from django.shortcuts import render
from rest_framework import generics

from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer

# Create your views here.
class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BlogInstanceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer