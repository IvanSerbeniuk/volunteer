from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from .models import Event
from django.utils import timezone
from blog.models import Post


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
def home(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    recent_posts = Post.objects.all()[:3]
    is_home_page = True  
    return render(request, 'home.html', {'events': events, 'recent_posts':recent_posts, 'is_home_page':is_home_page}, )#{'recent_posts': recent_posts}



def team(request):
    is_team_page = True  
    return render(request, 'team.html', {'is_team_page':is_team_page})



import json
import liqpay
from django.http import JsonResponse
from .models import Donation

liqpay_private_key = 'sandbox_997Trh625acVmzO9c2Syd5EGA7D31eTQDgfYuufG'
public_key='sandbox_i97618994403'

def liqpay_callback(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        signature = request.POST.get('signature')

        # Проверка подписи LiqPay
        liqpay_private_key = 'sandbox_997Trh625acVmzO9c2Syd5EGA7D31eTQDgfYuufG'
        liqpay_obj = liqpay.LiqPay(public_key='sandbox_i97618994403', private_key=liqpay_private_key)
        is_signature_valid = liqpay_obj.verify_signature(data, signature)

        if is_signature_valid:
            payment_data = json.loads(data)
            name = payment_data.get('name') 
            email = payment_data.get('email')  
            amount = payment_data.get('options')

            # Сохранение данных о пожертвовании в базе данных Django
            donation = Donation(name=name, email=email, amount=amount)
            donation.save()

            return JsonResponse({'success': True})

    return JsonResponse({'success': False})


