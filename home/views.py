from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def home(request):
    return render(request, 'index.html')

def successMsg(request, args):
    amount = args
    return render(request, 'templates/donation_success.html', {'amount': amount})

