from django.urls import path
from .views import parse_and_store

urlpatterns = [
    path('parse/', parse_and_store, name='parse_and_store'),
]
