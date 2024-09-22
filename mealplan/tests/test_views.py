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
        slug = slugify(self.data["name"])
        self.assertRedirects(self.response, f"/mealplans/{slug}")

    def test_saves_mealplan(self) -> None:
        self.assertTrue(Mealplan.objects.filter(name="Test Mealplan").exists())

