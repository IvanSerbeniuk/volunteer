from django.urls import path
from . import views

urlpatterns = [
    # path("sldf", views.index, name='index'),
    path("", views.home, name='home'),
]