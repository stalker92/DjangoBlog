from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.contrib.auth.models import User
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(PostListView):
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorizedPostView(LoginRequiredMixin, UserPassesTestMixin):
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(AuthorizedPostView, DeleteView):
    success_url = '/'


class PostUpdateView(AuthorizedPostView, UpdateView):
    fields = ['title', 'content']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
