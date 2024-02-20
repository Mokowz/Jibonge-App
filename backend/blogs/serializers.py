from rest_framework import serializers
from .models import Blog, Tag

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Blog
        fields = '__all__'