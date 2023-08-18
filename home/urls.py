from django.urls import path
from . import views
# from .views import donation

urlpatterns = [
    # path("sldf", views.index, name='index'),
    path("", views.home, name='home'),
    path('success/<str:args>/', views.successMsg, name='success'),
    path('donation/', views.donation, name='donation'),
]