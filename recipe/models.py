from django.db import models

# Create your models here.#


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    method = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

