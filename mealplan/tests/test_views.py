from django.template.defaultfilters import slugify
from django.test import TestCase
from mealplan.models import Mealplan

class RedirectionTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/mealplans/")

    def test_redirects(self) -> None:
        self.assertRedirects(self.response, "/mealplans/new")

class NewMealplanTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/mealplans/new")

    def test_uses_correct_template(self) -> None:
        self.assertTemplateUsed(self.response, "new.html")

class NewMealplanPostTest(TestCase):
    data = {
        "name": "Test Mealplan",
        "monday": "Monday's meal",
        "tuesday": "Tuesday's meal",
        "wednesday": "Wednesday's meal",
        "thursday": "Thursday's meal",
        "friday": "Friday's meal",
        "saturday": "Saturday's meal",
        "sunday": "Sunday's meal"
    }
    def setUp(self) -> None:
        self.response = self.client.post("/mealplans/new", data=self.data)

    def test_redirects_appropriately(self) -> None:
        slug = Mealplan.objects.filter(name="Test Mealplan")[0].slug
        self.assertRedirects(self.response, f"/mealplans/{slug}")

    def test_saves_mealplan(self) -> None:
        self.assertTrue(Mealplan.objects.filter(name="Test Mealplan").exists())

class ExistingMealplanDisplayTest(TestCase):
    def setUp(self) -> None:
        self.mealplan = Mealplan()
        self.mealplan.name = "Test Mealplan"
        self.mealplan.monday = "Monday's meal"
        self.mealplan.tuesday = "Tuesday's meal"
        self.mealplan.wednesday = "Wednesday's meal"
        self.mealplan.thursday = "Thursday's meal"
        self.mealplan.friday = "Friday's meal"
        self.mealplan.saturday = "Saturday's meal"
        self.mealplan.sunday = "Sunday's meal"
        self.mealplan.save()
        self.response = self.client.get(f"/mealplans/{self.mealplan.slug}")

    def test_uses_correct_template(self) -> None:
        self.assertTemplateUsed(self.response, "existing.html")

