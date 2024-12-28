from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from str2words.models import Word
# Create your views here.
@login_required
def str_history(request):

    objects = Word.objects.filter(user_id=request.user)
    context = {
        'word': objects
    }

    return render(request, 'templates/str_history.html', context)
