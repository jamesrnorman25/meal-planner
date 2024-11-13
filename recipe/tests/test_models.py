from django.test import TestCase
from recipe.models import Recipe, Ingredient

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUp(self) -> None:
        self.recipe = Recipe()
        self.recipe.name = "Tuna Sandwich"
        self.recipe.method = "Lorem ipsum dolor sit amet."
        self.recipe.save()

    def test_can_save_model(self) -> None:
        recipes = Recipe.objects.all()
        self.assertIn(self.recipe, recipes)


class IngredientModelTest(TestCase):
    def setUp(self) -> None:
        self.ingredient = Ingredient()
        self.ingredient.name = "Ingredient 1"
        self.ingredient.save()

    def test_can_save_model(self) -> None:
        ingredients = Ingredient.objects.all()
        self.assertIn(self.ingredient, ingredients)
