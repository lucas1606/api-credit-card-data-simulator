from django.db import models

# Create your models here.
class CreditCard(models.Model):
    id = models.CharField(max_length=50, primary_key= True)
    ui = models.CharField(max_length=50)
    Number = models.CharField(max_length=50)
    expiryData = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
