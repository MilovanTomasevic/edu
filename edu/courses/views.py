from django.shortcuts import render
from .models import Course, HeaderCourses
from django.views.generic import  DetailView, ListView

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