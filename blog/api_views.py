from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from .serializers import BlogSerializer
from .models import Blog
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

class BlogPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50

class BlogApiList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('author',)
    search_fields = ('title', 'text')
    pagination_class = BlogPagination

class BlogCreate(CreateAPIView):
    serializer_class = BlogSerializer