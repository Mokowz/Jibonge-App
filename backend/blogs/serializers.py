from rest_framework import serializers
from .models import Blog, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'tags', 'date_added', 'content']