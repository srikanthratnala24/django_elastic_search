from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=40)
    cc = models.IntegerField()
    gear = models.BooleanField()
    ev = models.BooleanField()


    def __str__(self):
        return self.name
    