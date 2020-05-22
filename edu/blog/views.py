from django.db.models import Count
from .models import Post, HeaderBlog, Category, PostView, Comment
from .forms import PostForm, CommentForm
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
    DeleteView,
)
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def blog_home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/blog.html', context)

def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

# def num_post(request):
#     user = get_object_or_404(User, username=request.kwargs.get('username'))
#     num_post = Post.objects.filter(author=user).count()
#     return render(request, 'blog/user_posts.html', {'num_post': num_post})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        posts = Post.objects.order_by('-date_posted')
        category_count = get_category_count()
        paginator = Paginator(posts, self.paginate_by)         
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context.update({
            'posts': posts,
            'header': HeaderBlog.objects.last(),
            'category_count' : category_count
        })
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context.update({
            'user_posts': Post.objects.filter(author=user).order_by('-date_posted'),
            'count': Post.objects.filter(author=user).count(),
        })
        return context

class CategoryesPostListView(ListView):
    model = Post
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(CategoryesPostListView, self).get_context_data(**kwargs)
        posts_by_category = Post.objects.filter(categories__title=self.kwargs.get('categories'))
        category_count = get_category_count()

        paginator = Paginator(posts_by_category, self.paginate_by)         
        page_number = self.request.GET.get('page')
        try:
            posts_by_category = paginator.page(page_number)
        except PageNotAnInteger:
            posts_by_category = paginator.page(1)
        except EmptyPage:
            posts_by_category = paginator.page(paginator.num_pages)

        context.update({
            'page_obj': posts_by_category,
            'header': HeaderBlog.objects.last(),
            'category_count' : category_count,
            'myP': 1,
        })
        return context

class PostDetailView(DetailView):
    model = Post
    form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        rposts = Post.objects.order_by('-date_posted')[:3]
        context.update({
            'rposts': rposts,
            'form': self.form
        })
        return context
    
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            content = form.cleaned_data.get("content")
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                # if parent object exist
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()
            new_comment = Comment.objects.get_or_create(
							user = request.user,
							content= content,
							post = post,
							parent = parent_obj,
						)

            return redirect(reverse("post-detail", kwargs={'pk': post.pk}))

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ('title', 'short_content', 'content', 'date_posted', 'image', 'categories')
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New'
        return context

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

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