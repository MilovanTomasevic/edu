from django.shortcuts import render
from .models import Course, HeaderCourses, Lesson
from django.views.generic import  DetailView, ListView, View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['course_date'] # - obrnuto
#     paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.order_by('course_date'),
            'header': HeaderCourses.objects.last(),
        })
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context.update({
            'rcourses': Course.objects.order_by('course_date')[:3],
        })
        return context

class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'object': lesson}
        return render(request, "courses/lesson_detail.html", context)