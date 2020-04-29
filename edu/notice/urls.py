from django.urls import path
from .views import NoticeListView, NoticeDetailView


urlpatterns = [
    path('', NoticeListView.as_view(), name='ecenter-notice'),
    path('<slug>/', NoticeDetailView.as_view(), name='ecenter-notice-single'),
]
