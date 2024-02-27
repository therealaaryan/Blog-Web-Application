from django.urls import path
from . import views


urlpatterns = [
    path('',views.BlogListView.as_view(), name='blog.list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog.detail'),
    path('new/', views.BlogCreateView.as_view()),
]