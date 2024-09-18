from django.test import TestCase
from mealplan.forms import MealplanForm

class MealplanFormTest(TestCase):
    def test_form_renders_correctly(self) -> None:
        form = MealplanForm()
        self.assertIn('placeholder="Name"', form.as_p())
        self.assertIn('placeholder="Monday"', form.as_p())
        self.assertIn('placeholder="Tuesday"', form.as_p())
        self.assertIn('placeholder="Wednesday"', form.as_p())
        self.assertIn('placeholder="Thursday"', form.as_p())
        self.assertIn('placeholder="Friday"', form.as_p())
        self.assertIn('placeholder="Saturday"', form.as_p())
        self.assertIn('placeholder="Sunday"', form.as_p())