from django.db import models

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=400)
    img = models.CharField(max_length=400)
    rental_type = models.CharField(max_length=400)
    rent_val = models.CharField(max_length=400)
    rep_val = models.CharField(max_length=400)
