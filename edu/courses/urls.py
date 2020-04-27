from django.urls import path
from .views import CourseDetailView, CoursesListView, LessonDetailView


urlpatterns = [
    path('', CoursesListView.as_view(), name='ecenter-courses'),
    path('<slug>/', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/<lesson_slug>/',LessonDetailView.as_view(), name='lesson-detail')
]
