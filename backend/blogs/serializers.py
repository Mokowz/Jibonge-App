from rest_framework import serializers
from .models import Blog, Tag, Author

from accounts.serializer import CusomUserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    user = CusomUserSerializer()

    class Meta:
        model = Author
        fields = ['id', 'user', 'profile_pic']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'tags', 'date_added', 'content']