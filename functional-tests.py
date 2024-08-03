import unittest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.close()

    def test_can_create_account(self) -> None:
        """Runs through the process of a user seeing the product and """
        # David has heard about a meal planning app.
        # He goes online to the meal planner's homepage.
        self.browser.get("http://localhost:8000")
        # He notices that "Home" is in the browser title and the page is welcoming.
        assert "Home" in self.browser.title
        self.assertIn("Home", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Welcome", header_text)

        # He invited to create an account.
        create_account_button = self.browser.find_element_by_id("id_create_account_button")
        self.assertEqual("Create Account", create_account_button.text)

        # Intrigued, David clicks on the button and is directed to the account creation page.
        create_account_button.click()
        time.sleep(1)
        self.assertIn("Create Account", self.browser.title)

        # He types his name (David) into the Username box and pasword123 into the password box (David doesn't understand cybersecurity).
        self.fail("TODO: Finish the test!")

        # When he hits enter, he logs in and is redirected to his dashboard.

if __name__ == "__main__":
    unittest.main()
