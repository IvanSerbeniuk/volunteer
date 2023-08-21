from django.urls import path
from . import views
# from .views import donation

urlpatterns = [
    path("", views.home, name='home'),
    path('success/<str:args>/', views.successMsg, name='success'),
    # path('', views.upcoming_events, name='upcoming_events'),
    # path('donation/', views.donation, name='donation'),
]