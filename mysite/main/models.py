from django.db import models

# Create your models here.


class Ingredient(models.Model):
    """
    Ingredient template. Includes ingredient name, standard unit for the ingredient
    and the minimum size available in shops.
    """
    INGREDIENT_UNIT = {
        "count": "",
        "g": "g",
        "ml": "ml",
        "tsp": "tsp",
        "tbsp": "tbsp"
    }
    ingredient_name = models.CharField(max_length=100)
    ingredient_count_unit = models.CharField(max_length=10, choices=INGREDIENT_UNIT)
    ingredient_min_buying_size = models.IntegerField()

class Recipe(models.Model):
    """Recipe record in the database. Includes name and prep time with units."""
    TIME_UNIT = {
        "min": "minutes",
        "hr": "hours"
    }
    recipe_name = models.CharField(max_length=300)
    recipe_prep_time = models.IntegerField()
    recipe_prep_time_unit = models.CharField(max_length=20, choices=TIME_UNIT)
    recipe_ingredients = models.ManyToManyField(Ingredient)

