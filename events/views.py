from django.shortcuts import render
from .models import Event, HeaderEvents
from django.views.generic import  DetailView, ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class EventsListView(ListView):
    model = Event
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(EventsListView, self).get_context_data(**kwargs)
        events = Event.objects.order_by('event_date')
        paginator = Paginator(events, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        context.update({
            'events': events,
            'header': HeaderEvents.objects.last(),
        })
        return context

class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context.update({
            'mevents': Event.objects.order_by('event_date')[:3],
        })
        return context