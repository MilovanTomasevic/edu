from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ecenter-home'),
    path('about/', views.about, name='ecenter-about'),
    path('courses/', views.courses, name='ecenter-courses'),
    path('course-single/', views.course_single, name='ecenter-course-single'),
    path('events/', views.events, name='ecenter-events'),
    path('event-single/', views.event_single, name='ecenter-event-single'),
    path('blog/', views.blog, name='ecenter-blog'),
    path('blog-single/', views.blog_single, name='ecenter-blog-single'),
    path('contact/', views.contact, name='ecenter-contact'),

    path('notice/', views.notice, name='ecenter-notice'),
    path('notice-single/', views.notice_single, name='ecenter-notice-single'),
    path('research/', views.research, name='ecenter-research'),
    path('scholarship/', views.scholarship, name='ecenter-scholarship'),
    path('teacher/', views.teacher, name='ecenter-teacher'),
    path('teacher-single/', views.teacher_single, name='ecenter-teacher-single'),

]

