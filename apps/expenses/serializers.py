from rest_framework import serializers
from .models import *


class ExpenseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        # fields = ['date','reference','beneficiary','category','type','payment','amount','comment']
        fields = '__all__'
