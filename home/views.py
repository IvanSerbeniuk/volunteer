from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Event
from django.utils import timezone
from blog.models import Post


def home(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    # recent_posts = Post.objects.all()[:3]
    recent_posts = Post.objects.all()[:3]
    return render(request, 'index.html', {'events': events, 'recent_posts': recent_posts}, )#{'recent_posts': recent_posts}

def successMsg(request, args):
    amount = args
    return render(request, 'templates/donation_success.html', {'amount': amount})


