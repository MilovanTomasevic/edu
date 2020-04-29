from django.shortcuts import render
from .models import Scholarship, HeaderScholarship
from django.views.generic import (
    ListView,
)

class ScholarshipListView(ListView):
    model = Scholarship
    # template_name = 'scholarship/scholarship_list.html'

    def get_context_data(self, **kwargs):
        context = super(ScholarshipListView, self).get_context_data(**kwargs)
        context.update({
            'scholarship': Scholarship.objects.last(),
            'header': HeaderScholarship.objects.last(),
        })
        return context