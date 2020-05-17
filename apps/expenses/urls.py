from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('expense_list/', views.expense_list, name='expense_list'),
]