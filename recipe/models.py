from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from time import time
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    method = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def save(self):
        self.slug = slugify(f"{self.name} {time()}")


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
