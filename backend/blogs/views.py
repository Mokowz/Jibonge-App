from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer

# Create your views here.
class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class TagListView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer