from django.db import models

# Create your models here.
class Rental(models.Model):
    img = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    rental_type = models.CharField(max_length=400)
    rent_val = models.IntegerField(max_length=100)
    rep_val = models.IntegerField(max_length=100)
    quant = models.IntegerField(max_length=100)
