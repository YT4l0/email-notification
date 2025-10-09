# api/urls.py

from django.urls import path
from .views import NotificationView

urlpatterns = [
    path('notify/', NotificationView.as_view(), name='notify'),
]