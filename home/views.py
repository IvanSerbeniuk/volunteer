from django.shortcuts import render
from django.http import HttpResponse
# from .models import ToDoList, Item
# Create your views here.


def home(request):
    return render(request, 'index.html')