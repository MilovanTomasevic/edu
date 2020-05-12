# from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course

class ChartView(TemplateView):
    template_name = 'analysis/analysis.html'

    def get_context_data(self, **kwargs):
        context = super(ChartView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

