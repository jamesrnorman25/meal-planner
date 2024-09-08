import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):
    username = "David"
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
        assert "Home" in self.browser.title
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
        password_box.send_keys("i@N7bR4ASnL0q$")
        password_confirmation_box.send_keys("i@N7bR4ASnL0q$")

        # When he hits enter, he logs in and is redirected to his dashboard.
        password_confirmation_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertIn("Dashboard - David", self.browser.title)

# class VisitorLoginTest(LiveServerTestCase):
#     username = "David"
#     password = "password123"

#     def setUp(self) -> None:
        
#         self.browser = webdriver.Firefox()

    
#     def tearDown(self) -> None:
#         self.browser.close()
        

if __name__ == "__main__":
    unittest.main()
