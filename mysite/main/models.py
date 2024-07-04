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

    def __str__(self) -> str:
        return self.ingredient_name

class Recipe(models.Model):
    """Recipe record in the database. Includes name and prep time with units."""
    TIME_UNIT = {
        "min": "minutes",
        "hr": "hours"
    }
    recipe_name = models.CharField(max_length=300)
    recipe_prep_time = models.IntegerField()
    recipe_prep_time_unit = models.CharField(max_length=20, choices=TIME_UNIT)
    recipe_ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    
    def __str__(self):
        return self.recipe_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.recipe.recipe_name} - {self.ingredient.ingredient_name}"
