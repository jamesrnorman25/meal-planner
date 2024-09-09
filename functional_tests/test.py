import unittest
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):
    username = "David"
    password = "i@N7bR4ASnL0q$"
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.close()
        

    def test_can_create_account(self) -> None:
        """Runs through the process of a user seeing the product and signing up."""
        # David has heard about a meal planning app.
        # He goes online to the meal planner's homepage.
        self.browser.get(self.live_server_url)
        # He notices that "Home" is in the browser title and the page is welcoming.
        self.assertIn("Home", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Welcome", header_text)

        # He invited to create an account.
        create_account_link = self.browser.find_element(By.ID, "id_link_create_account")
        self.assertEqual("Create Account", create_account_link.text)

        # Intrigued, David clicks on the link and is directed to the account creation page.
        create_account_link.click()
        time.sleep(1)
        self.assertIn("Create Account", self.browser.title)

        # He types his name (David) into the Username box and i@N7bR4ASnL0q$ into the password box (David has a very good memory and really understands cybersecurity)
        # before pressing Enter.
        username_box = self.browser.find_element(By.ID, "id_username")
        password_box = self.browser.find_element(By.ID, "id_password1")
        password_confirmation_box = self.browser.find_element(By.ID, "id_password2")
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_confirmation_box.send_keys(self.password)

        # When he hits enter, he logs in and is redirected to his dashboard.
        password_confirmation_box.send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertIn(f"Dashboard - {self.username}", self.browser.title)

        # Satisfied, he clicks on the log out button and is redirected back to the homepage.
        logout_button = self.browser. find_element(By.ID, "id_link_logout")
        logout_button.click()
        time.sleep(3)
        self.assertIn("Home", self.browser.title)


class ExistingUserLoginTest(LiveServerTestCase):
    username = "David"
    password = "password123"

    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.browser = webdriver.Firefox()

    
    def tearDown(self) -> None:
        self.browser.close()
        User.objects.filter(username=self.username).delete()

    def test_user_can_log_in(self) -> None:
        # After a while, David wants to return to the website.
        self.browser.get(self.live_server_url)
        # He clicks on the log in link in the navbar and is directed to the login page.
        login_link = self.browser.find_element(By.ID, "id_link_login")
        login_link.click()
        time.sleep(1)
        self.assertIn("Login", self.browser.title)
        
        # David types his username and password into the required boxes and hits Enter
        username_box = self.browser.find_element(By.ID, "id_username")
        password_box = self.browser.find_element(By.ID, "id_password")
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(3)

        # As before, he is redirected to his dashboard.
        self.assertIn(f"Dashboard - {self.username}", self.browser.title)
        

if __name__ == "__main__":
    unittest.main()
