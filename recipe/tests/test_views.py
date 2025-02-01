from django.test import RequestFactory, TestCase
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

    def test_redirects_if_not_authenticated(self) -> None:
        self.client.logout()
        response = self.client.get("/recipes/new")
        self.assertRedirects(response, "/Login")

class NewRecipePostTest(TestCase):
    username="test_user"
    password="test_password"
    valid_data = {'name': ['Tuna sandwich'], 
                  'form-TOTAL_FORMS': ['3'], 
                  'form-INITIAL_FORMS': ['0'], 
                  'form-MIN_NUM_FORMS': ['1'], 
                  'form-MAX_NUM_FORMS': ['1000'], 
                  'form-0-ingredient': ['1'], 
                  'form-0-quantity': ['20'], 
                  'form-0-DELETE': [''], 
                  'form-1-ingredient': ['2'], 
                  'form-1-quantity': ['1'], 
                  'form-2-ingredient': ['3'], 
                  'form-2-quantity': ['10'], 
                  'method': ['1. Butter two slices of bread.\r\n        2. Put tuna on one slice of bread.\r\n        3. Put the other slice on top.']}
    def setUp(self) -> None:
        bread = Ingredient.objects.create(name="Bread")
        bread.save()
        tuna = Ingredient.objects.create(name="Tuna")
        tuna.save()
        butter = Ingredient.objects.create(name="Butter")
        butter.save()
        self.user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        self.user.save()

    def tearDown(self):
        self.client.logout()

    def test_can_create_recipe(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post("/recipes/new", self.valid_data)
        slug = Recipe.objects.get(name="Tuna sandwich").slug
        self.assertRedirects(response, f"/recipes/{slug}")

    def test_rejects_if_form_invalid(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post("/recipes/new", {"name": "Tuna sandwich"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "new_recipe.html")

class ViewRecipeTest(TestCase):
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

    def test_redirects_if_not_authenticated(self) -> None:
        response = self.client.get(f"/recipes/{self.slug}")
        self.assertRedirects(response, "/Login")
        

class EditRecipeTest(TestCase):

    def setUp(self) -> None:
        self.username="test_user"
        self.password="test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        self.bread = Ingredient.objects.create(name="Bread")
        self.bread.save()
        self.butter = Ingredient.objects.create(name="Butter")
        self.butter.save()
        self.recipe = Recipe(name="Bread and butter", method="Put the butter on the bread.", user=self.user)
        self.recipe.save()
        self.recipe_ingredient_1 = RecipeIngredient.objects.create(ingredient=self.bread, recipe=self.recipe, quantity=1)
        self.recipe_ingredient_2 = RecipeIngredient.objects.create(ingredient=self.butter, recipe=self.recipe, quantity=10)
        self.recipe_ingredient_1.save()
        self.recipe_ingredient_2.save()
        self.valid_data = {'name': ['Bread and butter'], 
                  'form-TOTAL_FORMS': ['2'], 
                  'form-INITIAL_FORMS': ['0'], 
                  'form-MIN_NUM_FORMS': ['1'], 
                  'form-MAX_NUM_FORMS': ['1000'], 
                  'form-0-ingredient': ['1'], 
                  'form-0-quantity': ['1'], 
                  'form-1-ingredient': ['2'], 
                  'form-1-quantity': ['10'],
                  'method': ['1. Slice the bread.\r\n        2. Spread the butter on the bread.']}
        self.slug = self.recipe.slug
        self.client.force_login(self.user)

    def tearDown(self):
        self.client.logout()

    def test_post_saves_correctly(self) -> None:
        response = self.client.post(f"/recipes/{self.recipe.slug}/edit", data=self.valid_data)
        self.assertRedirects(response, f"/recipes/{self.slug}")
        self.assertEqual(Recipe.objects.get(slug=self.slug).method, self.valid_data["method"][0])
    
    def test_redirects_if_not_authenticated(self) -> None:
        self.client.logout()
        response = self.client.get(f"/recipes/{self.slug}/edit")
        self.assertRedirects(response, "/Login")

    def test_correct_template_used(self) -> None:
        response = self.client.get(f"/recipes/{self.slug}/edit")
        self.assertTemplateUsed(response, "edit_recipe.html")
