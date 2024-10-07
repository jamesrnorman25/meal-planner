"""Tests Mealplan model and its associated form."""

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from mealplan.models import Mealplan

class MealplanModelTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.mealplan = Mealplan()
        self.mealplan.name = "Test Mealplan"
        self.mealplan.monday = "Monday's meal"
        self.mealplan.tuesday = "Tuesday's meal"
        self.mealplan.wednesday = "Wednesday's meal"
        self.mealplan.thursday = "Thursday's meal"
        self.mealplan.friday = "Friday's meal"
        self.mealplan.saturday = "Saturday's meal"
        self.mealplan.sunday = "Sunday's meal"
        self.mealplan.user = user
        self.mealplan.save()

    def test_can_save_and_retrieve_mealplans(self) -> None:
        saved_items = Mealplan.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].name, "Test Mealplan")

    def test_mealplan_slug_works_correctly(self) -> None:
        self.assertRegex(Mealplan.objects.all()[0].slug, f"{slugify(self.mealplan.name)}-.+")
