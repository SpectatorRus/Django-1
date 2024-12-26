from django.shortcuts import render
from str2words.forms import Str2Words


def count_numbers(data: list ) -> int:
    count = 0
    for i in data:
        try:
            i = int(i)
            count += 1
        except ValueError:
            pass
    return count

# Create your views here.
def str2words_page(request):
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
    print(words_count, numbers_count)
    return render(request, 'templates/words.html', context)
