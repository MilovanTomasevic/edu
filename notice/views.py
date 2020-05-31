from django.shortcuts import render
from .models import Notice, HeaderNotice
from django.views.generic import  DetailView, ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class NoticeListView(ListView):
    model = Notice
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        notice = Notice.objects.order_by('-notice_date')
        paginator = Paginator(notice, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            notice = paginator.page(page)
        except PageNotAnInteger:
            notice = paginator.page(1)
        except EmptyPage:
            notice = paginator.page(paginator.num_pages)

        context.update({
            'notice': notice,
            'header': HeaderNotice.objects.last(),
        })
        return context

class NoticeDetailView(DetailView):
    model = Notice
