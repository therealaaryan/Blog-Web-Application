from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
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
    filter_fields = ('author', 'id')
    search_fields = ('title', 'text')
    pagination_class = BlogPagination
    
class BlogCreate(CreateAPIView):
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        blog_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('blog_data_{}'.format(blog_id))
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            blog = response.data
            from django.core.cache import cache
            cache.set('blog_data_{}'.format(blog['id']), {
                'title' : blog['title'],
                'text' : blog['text'],
                'author' : blog['author'],
            })
        return response