import unittest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from .utils import wait_for

MAX_WAIT = 3  # Max wait for browser load.
WAIT_STEP = 0.5  # Wait step for browser load.


class NewRecipeTest(StaticLiveServerTestCase):
    username = "test_user"
    password = "test_password123"
    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        cookie = self.client.cookies["sessionid"]
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        self.browser.add_cookie({"name": "sessionid", "value": cookie.value, "secure": False, "path": '/'})
        self.browser.refresh()

    def tearDown(self) -> None:
        self.browser.close()

    def test_create_recipe_manually(self) -> None:
        # David wants to create a new recipe, so he navigates to his dashboard.
        self.browser.get(f"{self.live_server_url}/Dashboard")

        # He looks for the recipe section and clicks on the "New Recipe" button
        new_recipe_button = self.browser.find_element(By.ID, "id_link_new_recipe")
        new_recipe_button.click()

        # He is taken to a page marked "New Recipe"
        wait_for(lambda: self.assertIn(self.browser.current_url, "recipes/new"), MAX_WAIT, WAIT_STEP)
        page_header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(page_header.text, "New Recipe")
        
        # He enters the recipe named Tuna Sandwich
        # Ingredients: Bread, Tuna, Butter
        # Method:
        # 1. Butter two slices of bread.
        # 2. Put tuna on one slice of bread.
        # 3. Put the other slice on top.
        recipe_name = self.browser.find_element(By.ID, "id_recipe_name")
        recipe_name.send_keys("Tuna sandwich")
        add_ingredient_button = self.browser.find_element(By.ID, "id_button_add_ingredient")
        add_ingredient_button.click()
        add_ingredient_button.click()
        ingredient_fields = self.browser.find_elements(By.ID, "id_field_ingredient")
        for field, ingredient in zip(ingredient_fields, ["Bread", "Tuna", "Butter"]):
            field.send_keys(ingredient)
        method_field = self.browser.find_element(By.TAG_NAME, "textarea")
        method_field.send_keys(
            """1. Butter two slices of bread.
        2. Put tuna on one slice of bread.
        3. Put the other slice on top."""
        )
        submit_button = self.browser.find_element(By.ID, "id_button_submit")
        submit_button.click()

        # He is redirected to a new page for the recipe.
        wait_for(lambda: self.assertIn("Tuna sandwich".upper(), self.browser.title.upper()), MAX_WAIT, WAIT_STEP)
