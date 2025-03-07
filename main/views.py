from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'main/index.html')


def curr_datetime(request):
    now = datetime.now()
    context = {
            'curr_date': now.strftime("%d.%m.%y"),
            'curr_time': now.strftime("%H:%M:%S")
        }
    return render(request, 'main/datetime.html', context)  

