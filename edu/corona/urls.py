from django.urls import path
from .views import CoronaView, CountryView

urlpatterns = [
    path('', CoronaView.as_view(), name='ecenter-corona'),
    path('country', CountryView.as_view(), name='ecenter-country'),
]