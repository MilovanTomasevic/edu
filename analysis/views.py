
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course

from rest_framework.views import APIView
from rest_framework.response import Response
class ChartView(TemplateView):
    template_name = 'analysis/analysis.html'

    def get_context_data(self, **kwargs):
        context = super(ChartView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context.update({
            'courses': courses,
            'header_api': 'Analysis',
            'message_api': 'Chart',
        })
        return context


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format = None):

        labels = [c.title for c in Course.objects.all()]

        chartLabel = "Price (€) of Courses"
        chartdata = [c.price for c in Course.objects.all()]
        data ={
            "labels":labels,
            "chartLabel":chartLabel,
            "chartdata":chartdata,
             }
        return Response(data)