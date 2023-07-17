from django.contrib.gis.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    phonenumber = models.CharField(max_length=15)
    language = models.CharField(max_length=3)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    information = models.PolygonField()
