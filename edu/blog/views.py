from .models import Post, HeaderBlog
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def blog_home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/blog.html', context)

# def num_post(request):
#     user = get_object_or_404(User, username=request.kwargs.get('username'))
#     num_post = Post.objects.filter(author=user).count()
#     return render(request, 'blog/user_posts.html', {'num_post': num_post})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
#     paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.order_by('-date_posted'),
            'header': HeaderBlog.objects.last(),
        })
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context.update({
            'user_posts': Post.objects.filter(author=user).order_by('-date_posted'),
            'count': Post.objects.filter(author=user).count(),
        })
        return context

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'rposts': Post.objects.order_by('-date_posted')[:3],

        })
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ('title', 'short_content', 'content', 'date_posted', 'image', 'categories')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # fields = ('title', 'short_content', 'content', 'date_posted', 'image', 'categories')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False