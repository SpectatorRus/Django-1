from django.shortcuts import render
from expression.models import CalcHistory

# Create your views here.
def clear_page(request):
    status = ""
    try:
        cals = CalcHistory.objects.all()
        for i in cals:
            CalcHistory.delete(i)
        status = "История выражений очищена"
    except Exception:
        status = "что-то не захотелось удаляться :)"

    return render(request, "templates/clear.html", context={"status": status})