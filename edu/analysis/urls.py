from django.conf.urls import url
from django.contrib import admin

from .views import ChartView

urlpatterns = [
    url('', ChartView.as_view(), name='analysis'),
]