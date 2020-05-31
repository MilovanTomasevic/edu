from django.urls import path
from . import views

urlpatterns = [
    path('',views.send_mail, name='ecenter-contact'),
]