from django.test import TestCase
from django.contrib.auth.models import User

from recipe.models import Ingredient, Recipe, RecipeIngredient

class NewRecipeGetTest(TestCase):
    username="test_user"
    password="test_password"
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        self.user.save()

    def tearDown(self):
        self.client.logout()

    def test_can_get_page(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get("/recipes/new")
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get("/recipes/new")
        self.assertTemplateUsed(response, "new_recipe.html")

    def test_redirects_if_anonymous(self) -> None:
        response = self.client.get("/recipes/new")
        self.assertRedirects(response, "/Login")

class ViewRecipeGetTest(TestCase):
    username="test_user"
    password="test_password"
    ingredients = [("Bread", 1), ("Butter", 10)]
    recipe = {"name": "Bread and butter", "method": "Put the butter on the bread."}
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        recipe = Recipe(name=self.recipe["name"], method=self.recipe["method"], user=self.user)
        recipe.save()
        self.slug = recipe.slug
        for ingredient_name in self.ingredients:
            ingredient = Ingredient.objects.create(name=ingredient_name[0])
            
            recipe_ingredient = RecipeIngredient.objects.create(ingredient=ingredient, recipe=recipe, quantity=ingredient_name[1])

    def tearDown(self):
        self.client.logout()

    def test_correct_template_used(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(f"/recipes/{self.slug}")
        self.assertTemplateUsed(response, "existing_recipe.html")
        
    
