from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('expense_list/', views.expense_list, name='expense_list'),
    path('api/expenses/', views.expense_api_list, name='api_expenses_list'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:pk>', views.category_details, name='category_details'),
]