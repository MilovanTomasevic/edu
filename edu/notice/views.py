from django.shortcuts import render
from .models import Notice, HeaderNotice
from django.views.generic import  DetailView, ListView

class NoticeListView(ListView):
    model = Notice

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        context.update({
            'notice': Notice.objects.order_by('-notice_date'),
            'header': HeaderNotice.objects.last(),
        })
        return context

class NoticeDetailView(DetailView):
    model = Notice
