from django.test import TestCase
from django.contrib.auth.models import User

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

