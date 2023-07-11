from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def charge(request):
    amount = 5
    if request.method == "POST":
        print('data: ', request.POST)
    
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'success.html', {'amount': amount})