from django.db import models



class Bank(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveBigIntegerField(default=100000000)