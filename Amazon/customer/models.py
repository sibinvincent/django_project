from django.db import models


## Commands for eql light migrations
## python manage.py makemigrations
## pythoon manage.py migrate
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=500)


#ORM Queries
