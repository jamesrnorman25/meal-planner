from django.test import TestCase
from recipe.forms import RecipeForm, RecipeIngredientForm

class RecipeFormTest(TestCase):
    def setUp(self) -> None:
        self.form = RecipeForm()

    def test_form_renders(self) -> None:
        self.assertIn('name="name"', self.form.as_p())
        self.assertIn('name="method"', self.form.as_p())

class RecipeIngredientFormTest(TestCase):
    def setUp(self) -> None:
        self.form = RecipeIngredientForm()

    def test_form_renders_correctly(self) -> None:
        self.assertIn('name="ingredient"', self.form.as_p())
        self.assertIn('name="quantity"', self.form.as_p())
