from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<username>', views.UserPostListView.as_view(), name='blog-user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-create'),
]