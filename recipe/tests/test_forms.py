from django.test import TestCase
from recipe.forms import RecipeForm

class RecipeFormTest(TestCase):
    def setUp(self) -> None:
        self.form = RecipeForm()

    def test_form_renders(self) -> None:
        self.fail(self.form.as_p())
