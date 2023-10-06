from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('team/', views.team, name='team'),
    path('liqpay_callback/', views.liqpay_callback, name='liqpay_callback'),
    # path('your-django-endpoint/', views.your_django_endpoint, name='your-django-endpoint'),
]