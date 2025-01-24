from django.shortcuts import render
from expression.models import CalcHistory

# Create your views here.
def clear_page(request):
    """
    Очищает историю вычислений(:ref:`CalcHistory`) с ulr(/expression и /new). \n
    Если всё успешно status = "История выражений очищена" иначе \n
    Если что-то пошло не так status =  "что-то не захотелось удаляться :)"  \n
    :param request: \n
    :return: render(request, "clear.html", context={"status": status}) \n
    """
    status = ""
    try:
        cals = CalcHistory.objects.all()
        for i in cals:
            CalcHistory.delete(i)
        status = "История выражений очищена"
    except Exception:
        status = "что-то не захотелось удаляться :)"

    return render(request, "clear.html", context={"status": status})