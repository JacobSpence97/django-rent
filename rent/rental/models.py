from django.db import models

# Create your models here.
class Rental(models.Model):
    img = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    rental_type = models.CharField(max_length=400)
    rent_val = models.IntegerField()
    rep_val = models.IntegerField()
    quant = models.IntegerField()
