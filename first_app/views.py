from django.shortcuts import render


def index_page(request):
    context = {
        "name": 'Alexander',
        "page_count": 1
    }
    return render(request, "templates/index.html", context)
