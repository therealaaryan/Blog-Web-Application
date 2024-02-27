from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/list_view.html'

    def get_queryset(self):
        return self.request.user.blogs.all()

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

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete_view.html'
    success_url = '/blogs/'

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blogs/'