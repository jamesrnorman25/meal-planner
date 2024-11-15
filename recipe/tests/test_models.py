from django.test import TestCase
from recipe.models import Recipe, Ingredient

import logging
logger = logging.getLogger(__name__)

# Create your tests here.

class RecipeModelTest(TestCase):
   
    def setUp(self) -> None:
       self.recipe = Recipe()
       self.recipe.save()
   
    def test_default_name(self) -> None:
        self.assertEqual(self.recipe.name, "")

    def test_default_method(self) -> None:
        self.assertEqual(self.recipe.method, "")

    def test_default_ingredients(self) -> None:
        self.assertEqual(self.recipe.ingredients.all().count(), 0)

class IngredientModelTest(TestCase):
    def setUp(self) -> None:
        self.ingredient = Ingredient()
        self.ingredient.name = "Ingredient 1"
        self.ingredient.save()

    def test_can_save_model(self) -> None:
        ingredients = Ingredient.objects.all()
        self.assertIn(self.ingredient, ingredients)
