from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def logout_page(request):
    if request.POST:
        logout(request)
        return redirect('/auth')
    return render(request, 'logout.html', {})
