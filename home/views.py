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
    is_home_page = True  
    return render(request, 'index.html', {'events': events, 'recent_posts': recent_posts, 'is_home_page':is_home_page}, )#{'recent_posts': recent_posts}



def team(request):
    is_team_page = True  
    return render(request, 'team.html', {'is_team_page':is_team_page})