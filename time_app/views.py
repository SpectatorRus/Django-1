import datetime
from django.shortcuts import render

def time_page(request):
    """
    Выводит время в формате\n
    1. день/месяц/год \n
    2. час/минуты/секунды \n
    :param request:
    :return: render(request, 'time.html', context)
    """
    date = f"{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}"
    time = f"{datetime.datetime.now().hour}.{datetime.datetime.now().minute}.{datetime.datetime.now().second}"
    context = {
        "time": time,
        "date": date
    }
    return render(request, 'time.html', context)
