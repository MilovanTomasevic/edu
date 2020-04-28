from django.shortcuts import render
from .models import Research, HeaderResearch
from django.views.generic import (
    ListView,
)

class ResearchListView(ListView):
    model = Research

    def get_context_data(self, **kwargs):
        context = super(ResearchListView, self).get_context_data(**kwargs)
        context.update({
            'research': Research.objects.all(),
            'header': HeaderResearch.objects.last(),
        })
        return context