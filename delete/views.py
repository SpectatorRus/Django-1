from django.shortcuts import render
from expression.models import CalcHistory

# Create your views here.
def delete_page(request):
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
