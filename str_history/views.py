from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from str2words.models import Word
# Create your views here.
@login_required
def str_history(request):
    """
    Выводит все :ref:`Word` \n
    :param request:
    :return: render(request, 'str_history.html', context)
    """
    objects = Word.objects.filter(user_id=request.user)
    context = {
        'word': objects
    }

    return render(request, 'str_history.html', context)
