from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from mealplan.models import Mealplan
from django.urls import reverse

class RedirectionTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        self.response = self.client.get("/mealplans/")

    def test_redirects(self) -> None:
        self.assertRedirects(self.response, "/mealplans/new")

class NewMealplanTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
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
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        self.response = self.client.post("/mealplans/new", data=self.data)

    def test_redirects_appropriately(self) -> None:
        slug = Mealplan.objects.filter(name="Test Mealplan")[0].slug
        self.assertRedirects(self.response, f"/mealplans/{slug}")

    def test_saves_mealplan(self) -> None:
        self.assertTrue(Mealplan.objects.filter(name="Test Mealplan").exists())

    def test_includes_user(self) -> None:
        self.assertIsNotNone(Mealplan.objects.filter(name="Test Mealplan")[0].user)

class InvalidMealplanPostTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        
    def test_handles_invalid_mealplan(self) -> None:
        response = self.client.post("/mealplans/new", data={})
        self.assertIsNotNone(response)

class LoggedOutNewMealplanTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/mealplans/new")
    
    def test_redirects_to_login(self) -> None:
        self.assertRedirects(self.response, reverse("login") + "?next=/mealplans/new")

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

class EditMealplanDisplayTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
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
        self.response = self.client.get(f"/mealplans/{self.mealplan.slug}/edit")

    def test_page_exists(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_uses_correct_template(self) -> None:
        self.assertTemplateUsed(self.response, "edit.html")

    def test_redirects_if_not_authenticated(self) -> None:
        self.client.logout()
        response = self.client.get(f"/mealplans/{self.mealplan.slug}/edit")
        self.assertRedirects(response, reverse("login") + f"?next=/mealplans/{self.mealplan.slug}/edit")


class EditMealplanPostTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
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
        self.response = self.client.post(f"/mealplans/{self.mealplan.slug}/edit", data={"name": "Test Mealplan", "monday": "New meal",
                                                                                        "tuesday": "Tuesday's meal", "wednesday": "Wednesday's meal",
                                                                                        "thursday": "Thursday's meal", "friday": "Friday's meal",
                                                                                        "saturday": "Saturday's meal", "sunday": "Sunday's meal"})
        
    def test_can_edit_mealplan(self) -> None:
        self.assertEqual(Mealplan.objects.get(name=self.mealplan.name).monday, "New meal")

    def test_redirects_correctly(self) -> None:
        self.assertRedirects(self.response, f"/mealplans/{self.mealplan.slug}")
