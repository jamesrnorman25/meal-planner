"""This is a collection of unit tests for the meal_planner app.
    :author: jamesrnorman25
"""

from django.test import TestCase

class HomepageTest(TestCase):

    def test_homepage_template_used(self) -> None:
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")

    def test_account_creation_template_used(self) -> None:
        response = self.client.get('/Create-Account')
        self.assertTemplateUsed(response, "create_account.html")
