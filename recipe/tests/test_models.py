from django.contrib.auth.models import User
from django.test import TestCase
from recipe.models import Recipe, Ingredient, RecipeIngredient
from unittest import skip, mock

import logging
logger = logging.getLogger(__name__)

# Create your tests here.
class RecipeModelTest(TestCase):
   
    def setUp(self) -> None:
       test_user = User.objects.create_user(username="test_user", password="test_password", is_active=1)
       self.recipe = Recipe(user=test_user)
       self.recipe.save()
   
    def test_default_name(self) -> None:
        self.assertEqual(self.recipe.name, "")

    def test_default_method(self) -> None:
        self.assertEqual(self.recipe.method, "")

    def test_can_delete_model(self) -> None:
        ingredient = Ingredient(name="Test Ingredient")
        ingredient.save()
        recipe_ingredient = RecipeIngredient(recipe=self.recipe, ingredient=ingredient, quantity=5)
        recipe_ingredient.save()
        self.recipe.delete()
        recipes = Recipe.objects.all()
        self.assertNotIn(self.recipe, recipes)
        self.assertEqual(RecipeIngredient.objects.all().count(), 0)

    # def test_default_ingredients(self) -> None:
    #     self.assertEqual(self.recipe.ingredients.all().count(), 0)

class IngredientModelTest(TestCase):
    def setUp(self) -> None:
        self.ingredient = Ingredient()
        self.ingredient.name = "Ingredient 1"
        self.ingredient.save()

    def test_can_save_model(self) -> None:
        ingredients = Ingredient.objects.all()
        self.assertIn(self.ingredient, ingredients)


# @skip("RecipeIngredient model is not implemented yet")
# class RecipeIngredientModelTest(TestCase):
#     def setUp(self) -> None:
#         self.recipe_ingredient = RecipeIngredient()
#         self.recipe_ingredient.save()

#     def test_can_save_model(self) -> None:
#         recipe_ingredients = RecipeIngredient.objects.all()
#         self.assertIn(self.recipe_ingredient, recipe_ingredients)
