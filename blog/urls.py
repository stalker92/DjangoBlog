from django.contrib import admin
from django.urls import path
from .views import (
    about,
    PostCreateView,
    PostListView,
    UserPostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView)

urlpatterns = [
    path('about/', about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<username>', UserPostListView.as_view(), name='blog-user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
]