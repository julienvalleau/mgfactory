from django.db import models
from django.db.models.base import Model
from commonbase.models import City

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
