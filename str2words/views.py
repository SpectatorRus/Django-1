from typing import List

from django.shortcuts import render
from str2words.forms import Str2Words

from django.contrib.auth.decorators import login_required

from str2words.models import Word
import datetime


def count_numbers(data: list) -> list[int | list[int]]:
    count = 0
    numbers_list = []
    for i in data:
        try:
            i = int(i)
            numbers_list.append(int(i))
            count += 1
        except ValueError:
            pass
    return [count, numbers_list]


# Create your views here.
@login_required
def str2words_page(request):
    """
    Принимает строку и разбирает её на слова, цифры и символы, записывает результат в :ref:`Word` \n
    Для подсчёта цифр используется функция count_numbers \n
    :param request:
    :return: render(request, 'words.html', context)
    """
    context = {
        'str2words_form': Str2Words()
    }
    if 'words' not in request.POST:
        return render(request, 'templates/words.html', context)

    data_form = Str2Words(request.POST)
    if not data_form.is_valid():
        return render(request, 'templates/words.html', context)

    words = data_form.cleaned_data["words"].split()
    words_count = len(words)
    numbers_count = count_numbers(words)
    date = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    time = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
    word = Word(
        date=date,
        time=time,
        inputtedString=data_form.cleaned_data["words"],
        words_count=words_count,
        symbols_count=len(data_form.cleaned_data["words"]),
        user=request.user
    )
    word.save()
    context["words"] = words
    context["numbers"] = numbers_count[1]
    return render(request, 'words.html', context)
