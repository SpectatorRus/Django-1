from django.shortcuts import render


def index_page(request):
    from da.urls import urlpatterns
    context = {
        "name": 'Alexander',
        "page_count": len(urlpatterns)-1
    }
    return render(request, "index.html", context)
