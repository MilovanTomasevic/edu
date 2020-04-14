from django.shortcuts import render

from .models import About

def aboutus(request):
    about = About.objects.last()
    peoples = about.peoples.all()

    template = 'about/about.html'
    context = {
        'about' : about,
        'peoples' : peoples
    }
    return render(request, template, context)