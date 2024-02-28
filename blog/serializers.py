from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    class Meta:
        model = Blog
        fields = ('title', 'text', 'author', 'id')