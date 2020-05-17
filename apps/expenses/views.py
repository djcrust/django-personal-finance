from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django_personal_finance import settings


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        return render(request, 'common/dashboard.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = settings.LOGIN_REDIRECT_URL
                print('OK')
                return redirect(redirect_to)
            else:
                context = {
                    'error': 'Your My Money account is disabled.',
                }
                return render(request, 'common/login.html',context)
        else:
            context = {
                'error': 'Invalid Login or Password.',
            }
            return render(request, 'common/login.html', context)
    else:
        context = {
            'error': '',
        }
        return render(request, 'common/login.html', context)


def logout_user(request):
    logout(request)
    context = {
        "form": '',
    }
    return render(request, 'common/login.html', context)