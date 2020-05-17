from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_personal_finance import settings

# Create your views here.


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        return render(request, 'common/dashboard.html')


def expense_list(request):
    pass


def expense_new(request):
    pass


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = settings.LOGIN_REDIRECT_URL
                return redirect(redirect_to)
            else:
                messages.error(request,'Your My Money account is disabled.')
                return render(request, 'common/login.html')
        else:
            messages.error(request,'Invalid Login or Password.')
            return render(request, 'common/login.html')
    else:
        return render(request, 'common/login.html')


def logout_user(request):
    logout(request)
    context = {
        "form": '',
    }
    return render(request, 'common/login.html', context)