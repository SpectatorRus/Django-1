from django.shortcuts import render
from expression.models import CalcHistory

def history_page(request):
    cals_history = CalcHistory.objects.all()

    return render(request, 'templates/history.html', {'cals_history': cals_history})