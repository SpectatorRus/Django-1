from django.shortcuts import render
from expression.models import CalcHistory

def history_page(request):
    """
    Отображает все :ref:`CalcHistory` пользователю \n
    :param request:
    :return: render(request, 'history.html', {'cals_history': cals_history})
    """
    cals_history = CalcHistory.objects.all()

    return render(request, 'history.html', {'cals_history': cals_history})