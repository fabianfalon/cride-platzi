"""Circles URLs."""

# Django
from django.urls import path

# Views
from cride.circles.views import list_circles

urlpatterns = [
    path('circles/', list_circles)
]
