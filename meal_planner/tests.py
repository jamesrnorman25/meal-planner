"""This is a collection of unit tests for the meal_planner app.
    :author: jamesrnorman25
"""

from django.test import TestCase

class HomepageTest(TestCase):

    def test_homepage_is_correct_2(self) -> None:
        response = self.client.get('/')
        self.assertContains(response, "<title>Home</title>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")
