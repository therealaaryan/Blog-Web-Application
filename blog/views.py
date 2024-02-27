from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/list_view.html'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/detail_view.html'

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog.list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

