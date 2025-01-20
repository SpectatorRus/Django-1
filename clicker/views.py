from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from clicker.models import ClickerData


@login_required
def clicker_page(request):
    if request.POST:
        # print(request.POST)
        hp = int(request.POST["hp"].split(' ')[1])
        iq = int(request.POST["iq"].split(' ')[1])
        happiness = int(request.POST["happiness"].split(' ')[1])
        try:
            clicker = ClickerData.objects.get(user_id=request.user.id)
            clicker.hp = hp
            clicker.iq = iq
            clicker.happiness = happiness
            clicker.save()
        except ObjectDoesNotExist:
            clicker = ClickerData(user_id=request.user.id,
                                  hp=hp,
                                  iq=iq,
                                  happiness=happiness)
            clicker.save()
    context = {}
    try:
        data = ClickerData.objects.get(user_id=request.user.id)
        context = {
            'hp': data.hp,
            'iq': data.iq,
            'happiness': data.happiness
        }
    except ObjectDoesNotExist:
        pass

    return render(request, 'clicker.html', context)
