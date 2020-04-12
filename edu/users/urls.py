from django.urls import path
from . import views
from .views import ProfileDetailView

urlpatterns = [
    path('', views.profile, name='ecenter-profile'),
    path('<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('edit/', views.update_profile, name='profile-update'),
]