from django.urls import path
from .views import manager

urlpatterns = [
    path('', manager, name='manager'),
]