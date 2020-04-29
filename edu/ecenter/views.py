from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def event_single(request):
    return render(request, 'event-single.html')

def notice(request):
    return render(request, 'notice.html')

def notice_single(request):
    return render(request, 'notice-single.html')

def teacher(request):
    return render(request, 'teacher.html')

def teacher_single(request):
    return render(request, 'teacher-single.html')