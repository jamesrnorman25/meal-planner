import unittest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from .utils import wait_for
from recipe.models import Ingredient, Recipe, RecipeIngredient
from django.utils.text import slugify

MAX_WAIT = 3  # Max wait for browser load.
WAIT_STEP = 0.5  # Wait step for browser load.


class NewRecipeTest(StaticLiveServerTestCase):
    username = "test_user"
    password = "test_password123"
    def setUp(self) -> None:
        bread = Ingredient.objects.create(name="Bread")
        bread.save()
        tuna = Ingredient.objects.create(name="Tuna")
        tuna.save()
        butter = Ingredient.objects.create(name="Butter")
        butter.save()
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
        wait_for(lambda: self.assertIn("recipes/new", self.browser.current_url), MAX_WAIT, WAIT_STEP)
        page_header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(page_header.text, "New Recipe")
        
        # He enters the recipe named Tuna Sandwich
        # Ingredients: Bread, Tuna, Butter
        # Method:
        # 1. Butter two slices of bread.
        # 2. Put tuna on one slice of bread.
        # 3. Put the other slice on top.
        recipe_name = self.browser.find_element(By.ID, "id_name")
        recipe_name.send_keys("Tuna sandwich")
        add_ingredient_button = self.browser.find_element(By.CLASS_NAME, "add-row")
        add_ingredient_button.click()
        add_ingredient_button.click()
        # ingredient_fields = self.browser.find_elements(By.ID, "id_field_ingredient")
        for field_num, ingredient in zip(range(3), [("Bread", 2), ("Tuna", 1), ("Butter", 10)]):
            ingredient_field = Select(self.browser.find_element(By.ID, f"id_form-{field_num}-ingredient"))
            ingredient_field.select_by_visible_text(ingredient[0])
            quantity_field = self.browser.find_element(By.ID, f"id_form-{field_num}-quantity")
            quantity_field.send_keys(str(ingredient[1]))
        method_field = self.browser.find_element(By.TAG_NAME, "textarea")
        method_field.send_keys(
            """1. Butter two slices of bread.
        2. Put tuna on one slice of bread.
        3. Put the other slice on top."""
        )
        submit_button = self.browser.find_element(By.ID, "id_submit")
        submit_button.click()

        # He is redirected to a new page for the recipe.
        wait_for(lambda: self.assertIn(self.browser.title.upper(), "Tuna sandwich".upper()), MAX_WAIT, WAIT_STEP)


class EditRecipeTest(StaticLiveServerTestCase):
    username = "test_user"
    password = "test_password123"
    def setUp(self) -> None:
        bread = Ingredient.objects.create(name="Bread")
        bread.save()
        tuna = Ingredient.objects.create(name="Tuna")
        tuna.save()
        butter = Ingredient.objects.create(name="Butter")
        butter.save()
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.recipe = Recipe(name="Tuna sandwich", method="1. Butter two slices of bread.\n2. Put tuna on one slice of bread.", user=user)
        self.recipe.save()
        for ingredient, quantity in [(bread, 2), (tuna, 1), (butter, 10)]:
            recipe_ingredient = RecipeIngredient.objects.create(recipe=self.recipe, ingredient=ingredient, quantity=10)
            recipe_ingredient.save()
        self.client.force_login(user=user)
        cookie = self.client.cookies["sessionid"]
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        self.browser.add_cookie({"name": "sessionid", "value": cookie.value, "secure": False, "path": '/'})
        self.browser.refresh()

    def tearDown(self) -> None:
        self.browser.close()
        
    def test_can_edit_recipe(self):
        # David realised he didn't finish writing the method, so he navigates to his dashboard.
        self.browser.get(f"{self.live_server_url}/Dashboard")

        # He looks for the recipe section and clicks on the recipe he has.
        new_recipe_button = self.browser.find_element(By.NAME, f"link-edit-{slugify(self.recipe.name)}")
        new_recipe_button.click()

        # He is taken to a page marked "Edit Recipe"
        wait_for(lambda: self.assertIn("edit", self.browser.current_url), MAX_WAIT, WAIT_STEP)
        self.assertIn("recipe", self.browser.current_url)
        page_header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(page_header.text, "New Recipe")
        
        # He edits the method section.
        # Ingredients: Bread, Tuna, Butter
        # Method:
        # 1. Butter the first slice of bread.
        # 2. Put tuna on one slice of bread.
        # 3. Put the other slice on top.
        method_field = self.browser.find_element(By.TAG_NAME, "textarea")
        method_field.send_keys(
            """1. Butter two slices of bread.
        2. Put tuna on one slice of bread.
        3. Put the other slice on top."""
        )
        submit_button = self.browser.find_element(By.ID, "id_submit")
        submit_button.click()

        # He is redirected to the recipe's page.
        wait_for(lambda: self.assertIn(self.recipe.slug, self.browser.current_url), MAX_WAIT, WAIT_STEP)
        self.recipe.refresh_from_db()
        self.assertIn("Put the other slice on top.", self.recipe.method)
