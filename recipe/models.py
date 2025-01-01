from django.db import models

# Create your models here.#


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    method = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
