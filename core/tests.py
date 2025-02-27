"""This is a collection of unit tests for the meal_planner app.
    :author: jamesrnorman25
"""

from django.test import TestCase

from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.urls import reverse


import logging

logger = logging.getLogger(__name__)

class HomepageTest(TestCase):

    def test_homepage_template_used(self) -> None:
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")


class CreateAccountGetTest(TestCase):

    def test_account_creation_template_used(self) -> None:
        response = self.client.get('/Create-Account')
        self.assertTemplateUsed(response, "create_account.html")


class CreateAccountPostTest(TestCase):
    def setUp(self) -> None:
        self.username = "test"
        self.password = "i@N7bR4ASnL0q$"
        self.response = self.client.post("/Create-Account", data={"username": self.username, "password1": self.password, "password2": self.password})

    def test_saves_user(self) -> None:
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_logs_user_in(self) -> None:
        user = get_user(self.client)
        self.assertEqual(user.username, self.username)
        self.assertTrue(user.is_authenticated)
        

    def test__post_request_redirects(self) -> None:
        self.assertRedirects(self.response, '/Dashboard')

class CreateAccountInvalidPostTest(TestCase):
    def setUp(self) -> None:
        self.username="test"
        self.password="i@N7bR4ASnL0q$"
    
    def test_handles_invalid_password(self) -> None:
        response = self.client.post("/Create-Account", data={"username": self.username, "password1": self.password, "password2": ""})
        self.assertIsNotNone(response)
        

class DashboardLoggedInGetTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user)
        self.response = self.client.get("/Dashboard")

    def test_can_get_page(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_uses_dashboard_template(self) -> None:
        self.assertTemplateUsed(self.response, "dashboard.html")

class DashboardLoggedOutGetTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/Dashboard")

    def test_redirects_to_login(self) -> None:
        self.assertRedirects(self.response, reverse("login") + "?next=/Dashboard")


class LoginGetTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/Login")
    
    def test_can_get_page(self) -> None:
        self.assertEqual(self.response.status_code, 200)
    
    def test_uses_login_template(self) -> None:
        self.assertTemplateUsed(self.response, "login.html")


class LoginValidPostTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.response = self.client.post("/Login", data={"username": self.username, "password": self.password})

    def test_redirects_to_dashboard(self) -> None:
        self.assertRedirects(self.response, "/Dashboard")

    def test_logs_user_in(self) -> None:
        user = get_user(self.client)
        self.assertEqual(user.username, self.username)
        self.assertTrue(user.is_authenticated)

class LoginInvalidPostTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
    
    def test_handles_incorrect_password(self) -> None:
        response = self.client.post("/Login", data={"username": self.username, "password": "password124"})
        self.assertIsNotNone(response)

    def test_handles_incorrect_username(self) -> None:
        response = self.client.post("/Login", data={"username": self.username + "abc", "password": self.password})
        self.assertIsNotNone(response)

class LogoutTest(TestCase):
    username = "test"
    password = "password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        self.response = self.client.post("/Logout")

    def test_logs_user_out(self) -> None:
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_redirects_to_homepage(self) -> None:
        self.assertRedirects(self.response, "/")
