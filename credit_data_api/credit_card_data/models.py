from django.db import models

# Create your models here.
class CreditCard(models.Model):
    id = models.CharField(max_lenth=50)
    ui = models.CharField(max_lenth=50)
    Number = models.CharField(max_lenth=50)
    expiryData = models.CharField(max_lenth=50)
    type = models.CharField(max_lenth=50)
