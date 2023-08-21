from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Event
from django.utils import timezone


def home(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'index.html', {'events': events})

def successMsg(request, args):
    amount = args
    return render(request, 'templates/donation_success.html', {'amount': amount})


