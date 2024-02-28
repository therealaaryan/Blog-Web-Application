from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Blog
        fields = ('title', 'text', 'author', 'id')

    def validate_author(self, value):
        """
        Check if user exists in database and return User instance.
        """
        try:
            return User.objects.get(username=value)
        except ObjectDoesNotExist:
            raise ValidationError("User with username {} does not exist.".format(value))

    def create(self, validated_data):
        """
        Create and return a new `Blog` instance, given the validated data.
        """

        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Blog` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)

        if 'author' in validated_data:
            instance.author = validated_data['author']
        instance.save()
        return instance