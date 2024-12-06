import datetime
from django.shortcuts import render

def time_page(request):
    date = f"{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}"
    time = f"{datetime.datetime.now().hour}.{datetime.datetime.now().minute}.{datetime.datetime.now().second}"
    context = {
        "time": time,
        "date": date
    }
    return render(request, 'templates/time.html', context)
