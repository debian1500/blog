from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html', context)


def curr_datetime(request):
    now = datetime.now()
    context = {
            'curr_date': now.strftime("%d.%m.%y"),
            'curr_time': now.strftime("%H:%M:%S")
        }
    return render(request, 'main/datetime.html', context)  
