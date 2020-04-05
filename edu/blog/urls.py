# from django.urls import path
from .views import PostListView, PostDetailView
# (
#     PostListView,
#     PostDetailView
#     # PostCreateView,
#     # PostUpdateView,
#     # PostDeleteView,
#     # UserPostListView
# )

# urlpatterns = [
#     path('', PostListView.as_view(), name='blog-home'),
#     # path('blog/', views.blog, name='ecenter-blog'),
#     # path('blog-single/', views.blog_single, name='ecenter-blog-single'),
#     # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='ecenter-blog-single'),
#     # path('post/new/', PostCreateView.as_view(), name='post-create'),
#     # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
#     # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='ecenter-blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # path('ecenter-blog-single/', views.blog_single, name='ecenter-blog-single'),
]
