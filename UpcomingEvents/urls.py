from django.urls import path
from . import views

urlpatterns = [
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
]

