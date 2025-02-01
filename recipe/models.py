from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from time import time
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit_choices = [
        ("g", "g"),
        ("kg", "kg"),
        ("ml", "ml"),
        ("l", "l"),
        ("tbsp", "tbsp"),
        ("tsp", "tsp"),
        ("cup", "cup"),
        ("none", "No unit"),
        ("slices", "slices"),
    ]

    unit = models.CharField(max_length=100, choices=unit_choices, default="none")


    def __str__(self):
        return self.name if self.unit == "none" else f"{self.name} ({self.unit})"


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    method = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug or slugify(self.name) not in self.slug:
            self.slug = slugify(f"{self.name} {time()}")
        super().save()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
