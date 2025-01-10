from django.shortcuts import render, redirect
from auth.forms import Auth
from django.contrib.auth import authenticate, login

# Create your views here.
def auth_page(request):
    context = {
        "form": Auth()
    }
    if 'password' not in request.POST or 'username' not in request.POST:
        context["status"] = "не все поля заполнены"
        return render(request, 'registration/login.html', context)

    data = Auth(request.POST)

    if not data.is_valid():
        context["status"] = "некорректные данные"
        return render(request, 'registration/login.html', context)

    username = data.cleaned_data["username"]
    password = data.cleaned_data["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        print(context)
        context["status"] = "пользователь не найден"
        return render(request, 'login.html', context)

