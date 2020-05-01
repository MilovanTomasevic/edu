from django.shortcuts import render
from .models import Event, HeaderEvents
from django.views.generic import  DetailView, ListView

class EventsListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventsListView, self).get_context_data(**kwargs)
        context.update({
            'events': Event.objects.order_by('event_date'),
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