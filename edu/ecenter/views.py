from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, Baner, About, Training, Stories
from blog.models import Post
from courses.models import Course
from events.models import Event
from users.models import UserProfile
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect

def home(request):
    try:
        slider = Slider.objects.last()
        baner = Baner.objects.last()
        about = About.objects.last()
        courses = Course.objects.order_by('course_date')[:3]
        events = Event.objects.order_by('event_date')[:3]
        training = Training.objects.last()
        stories = Stories.objects.last()
        posts = Post.objects.order_by('-date_posted')[:3]
        profiles = UserProfile.objects.all()[:3]

        template = 'ecenter/index.html'
        context = {
            'slider' : slider,
            'baner' : baner,
            'about' : about,
            'courses' : courses,
            'events' : events,
            'training' : training,
            'stories' : stories,
            'posts' : posts,
            'profiles' : profiles
        }
        return render(request, template, context)
    except:
        messages.add_message(request, messages.INFO, 'It is necessary to insert data from the admin page')
        return HttpResponseRedirect('/admin')

def teacher(request):
    return render(request, 'teacher.html')

def teacher_single(request):
    return render(request, 'teacher-single.html')