from django.urls import path
from . import views, api_views


urlpatterns = [
    path('',views.BlogListView.as_view(), name='blog.list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog.detail'),
    path('new/', views.BlogCreateView.as_view()),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog.delete'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view()),
    path('api/', api_views.BlogApiList.as_view()),
    path('api/new', api_views.BlogCreate.as_view()),
]