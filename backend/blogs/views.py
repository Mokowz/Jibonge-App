from django.shortcuts import render
from rest_framework import generics, filters

from .models import Blog, Tag, Author
from .serializers import BlogSerializer, TagSerializer, AuthorSerializer

# Blog View
class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class BlogInstanceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Search View
class BlogSearchView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


# Tag View
class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# Author
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer