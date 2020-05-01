from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def teacher(request):
    return render(request, 'teacher.html')

def teacher_single(request):
    return render(request, 'teacher-single.html')