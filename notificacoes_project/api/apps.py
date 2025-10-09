from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

from django.urls import path
from .views import NotificationView

urlpatterns = [
    path('notify/', NotificationView.as_view(), name='notify'),
]
