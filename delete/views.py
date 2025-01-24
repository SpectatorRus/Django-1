from django.shortcuts import render
from expression.models import CalcHistory

# Create your views here.
def delete_page(request):
    """
    Удаляет последнюю запись из :ref:`CalcHistory` \n
    если всё хорошо status = "Удалено последнее выражение из истории" \n
    или status = "нет записей для удаления" \n
    неизвестная ошибка status = "что-то пошло не так :(" \n
    :param request:
    :return: render(request, 'delete.html', context={"status": status})
    """
    status = ""
    try:
        cals = CalcHistory.objects.last()
        if cals is not None:
            CalcHistory.delete(cals)
            status = "Удалено последнее выражение из истории"
        else:
            status = "нет записей для удаления"
    except Exception:
        status = "что-то пошло не так :("

    return render(request, 'delete.html', context={"status": status})
