from django.shortcuts import render
from .models import Course, HeaderCourses, Lesson, Category
from django.views.generic import  DetailView, ListView, View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q

class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['course_date'] # - obrnuto
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        courses = Course.objects.order_by('course_date')
        category = Category.objects.all()
        paginator = Paginator(courses, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)

        context.update({
            'courses': courses,
            'category':category,
            'header': HeaderCourses.objects.last(),
        })
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context.update({
            'rcourses': Course.objects.order_by('course_date')[:4],
        })
        return context

class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'object': lesson}
        return render(request, "courses/lesson_detail.html", context)

def is_valid_queryparam(param):
    return param != '' and param is not None


def FilterListView(request):
    paginate_by = 9
    courses_list = Course.objects.all()
    category = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_or_teacher = request.GET.get('title_or_teacher')
    short_content = request.GET.get('short_content')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    selected_category= request.GET.get('category')

    if is_valid_queryparam(title_contains_query):
        courses_list = courses_list.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(title_or_teacher):
        courses_list = courses_list.filter(Q(title__icontains=title_or_teacher)
                    | Q(teacher__name__icontains=title_or_teacher)
                    ).distinct()

    if is_valid_queryparam(short_content):
        courses_list = courses_list.filter(short_content__icontains=short_content)

    if is_valid_queryparam(min_price):
        courses_list = courses_list.filter(price__gte=min_price)

    if is_valid_queryparam(max_price):
        courses_list = courses_list.filter(price__lte=max_price)

    if is_valid_queryparam(date_min):
        courses_list = courses_list.filter(course_date__gte=date_min)

    if is_valid_queryparam(date_max):
        courses_list = courses_list.filter(course_date__lt=date_max)

    if is_valid_queryparam(selected_category) and selected_category != 'Choose...':
         courses_list = courses_list.filter(category__category_name=selected_category)

    paginator = Paginator(courses_list, paginate_by)
    page_number = request.GET.get('page')
    try:
        courses = paginator.page(page_number)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    context = {
        'page_obj': courses,
        'category':category,
        'header': HeaderCourses.objects.last(),
        'header_search': 'Search results',
        'myP': 1,
    }
    return render(request, "courses/filter.html", context)
