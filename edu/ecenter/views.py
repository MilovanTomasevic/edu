from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def course_single(request):
    return render(request, 'course-single.html')

def events(request):
    return render(request, 'events.html')

def event_single(request):
    return render(request, 'event-single.html')

def notice(request):
    return render(request, 'notice.html')

def notice_single(request):
    return render(request, 'notice-single.html')

def research(request):
    return render(request, 'research.html')

def scholarship(request):
    return render(request, 'scholarship.html')

def teacher(request):
    return render(request, 'teacher.html')

def teacher_single(request):
    return render(request, 'teacher-single.html')