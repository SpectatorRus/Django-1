from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def logout_page(request):
    if request.POST:
        logout(request)
        return redirect('/auth')
    return render(request, 'templates/logout.html', {})
