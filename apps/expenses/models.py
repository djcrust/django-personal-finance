from django.db import models


# Create your models here.

CHOICE_TYPE= [
    ('IN', 'IN'),
    ('OUT', 'OUT'),
]


CHOICE_PAYMENT = [
    ('1', 'CASH'),
    ('2', 'CB'),
    ('3', 'CHECK'),
    ('4', 'MOBILE BANKING'),
]


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField()
    reference = models.CharField(max_length=10, unique=True)
    beneficiary = models.CharField(max_length=255)
    category = models.ForeignKey(ExpenseCategory, related_name='category', on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=CHOICE_TYPE)
    payment = models.CharField(max_length=1, choices=CHOICE_PAYMENT)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    comment = models.CharField(max_length=255,null=True)
    removed = models.BooleanField(default=False)
    image_1 = models.ImageField(null=True)
    image_2 = models.ImageField(null=True)
    image_3 = models.ImageField(null=True)

    def __str__(self):
        return self.reference
