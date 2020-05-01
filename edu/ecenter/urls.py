from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='ecenter-home'),
    path('teacher/', views.teacher, name='ecenter-teacher'),
    path('teacher-single/', views.teacher_single, name='ecenter-teacher-single'),

]

