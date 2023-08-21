
from django.shortcuts import render
from .models import Event
from django.utils import timezone

def upcoming_events(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'upcoming_events.html', {'events': events})
