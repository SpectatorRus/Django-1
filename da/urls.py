"""
URL configuration for da project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from clicker.views import clicker_page
from first_app.views import index_page
from new.views import new_page
from str2words.views import str2words_page
from time_app.views import time_page
from calc_app.views import calc_page
from expression.views import expression_page
from history.views import history_page
from delete.views import delete_page
from clear.views import clear_page
from auth.views import auth_page
from logout.views import logout_page
from str_history.views import str_history

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('time/', time_page),
    path('calc/', calc_page),
    path('expression/', expression_page),
    path('history/', history_page),
    path('delete/', delete_page),
    path('clear/', clear_page),
    path('new/', new_page),
    path('str2words/', str2words_page),
    path('auth/', auth_views.LoginView.as_view()),
    path('logout/', logout_page),
    path('str_history/', str_history),
    path('clicker/', clicker_page)
]
