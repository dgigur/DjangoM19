from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=6, max_digits=8)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=6, max_digits=8)
    size = models.DecimalField(decimal_places=6, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)
