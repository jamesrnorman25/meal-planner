"""Models for meal plans."""
from django.db import models

class Mealplan(models.Model):
    name = models.CharField(max_length=100, default="")
    monday = models.CharField(max_length=100, default="")
    tuesday = models.CharField(max_length=100, default="")
    wednesday = models.CharField(max_length=100, default="")
    thursday = models.CharField(max_length=100, default="")
    friday = models.CharField(max_length=100, default="")
    saturday = models.CharField(max_length=100, default="")
    sunday = models.CharField(max_length=100, default="")
