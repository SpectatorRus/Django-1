from django.shortcuts import render


def index_page(request):
    """
    Отображает главную страницу и количество страниц на сайте не считая /admin \n
    :param request:
    :return: render(request, "index.html", context)
    """
    from da.urls import urlpatterns
    context = {
        "name": 'Alexander',
        "page_count": len(urlpatterns)-1
    }
    return render(request, "index.html", context)
