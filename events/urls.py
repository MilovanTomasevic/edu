from django.urls import path
from .views import EventsListView, EventDetailView

urlpatterns = [
    path('', EventsListView.as_view(), name='ecenter-events'),
    path('<slug>/', EventDetailView.as_view(), name='ecenter-events-single'),
]
