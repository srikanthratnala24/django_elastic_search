from django.db import models
from user.models import CustomUser
# Create your models here.

class Expense(models.Model):

    CATEGORY_OPTIONS = [
        ('ONLINE_SERVICES','ONLINE_SERVICES'),
        ('Travel','Travel'),
        ('Food','Food'),
        ('RENT','RENT'),
        ('OTHERS','OTHERS'),
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS,max_length=255)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)
    


