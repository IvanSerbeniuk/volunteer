from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('success/<str:args>/', views.successMsg, name='success'),
    path('team/', views.team, name='team'),
]