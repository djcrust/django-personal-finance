from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.expenses.models import *
from apps.expenses.serializers import *
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


@api_view(['GET','POST'])
def expense_api_list(request):

    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializers = ExpenseSerializers(expenses,many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ExpenseSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def category_list(request):

    if request.method == 'GET':
        categories = ExpenseCategory.objects.all()
        serializers = ExpenseCategorySerializers(categories,many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ExpenseCategorySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def category_details(request,pk):
    try:
        category = ExpenseCategory.objects.get(pk=pk)
    except ExpenseCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = ExpenseCategorySerializers(category)
        return Response(serializers.data)


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