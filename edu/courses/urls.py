from django.urls import path
from .views import CourseDetailView, CoursesListView

urlpatterns = [
    path('', CoursesListView.as_view(), name='ecenter-courses'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
]
