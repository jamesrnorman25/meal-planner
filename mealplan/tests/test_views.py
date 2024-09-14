from django.test import TestCase

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

