"""Tests Mealplan model and its associated form."""

from django.template.defaultfilters import slugify
from django.test import TestCase
from mealplan.models import Mealplan

class MealplanModelTest(TestCase):
    def test_can_save_and_retrieve_mealplans(self) -> None:
        mealplan = Mealplan()
        mealplan.name = "Test Mealplan"
        mealplan.monday = "Monday's meal"
        mealplan.tuesday = "Tuesday's meal"
        mealplan.wednesday = "Wednesday's meal"
        mealplan.thursday = "Thursday's meal"
        mealplan.friday = "Friday's meal"
        mealplan.saturday = "Saturday's meal"
        mealplan.sunday = "Sunday's meal"
        mealplan.save()
        saved_items = Mealplan.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].name, "Test Mealplan")
        self.assertEqual(saved_items[0].slug, slugify(mealplan.name))
