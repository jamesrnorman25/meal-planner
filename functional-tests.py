import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.close()

    def test_can_log_in(self) -> None:
        """Runs through the process of a user seeing the product and """
        # David has heard about a meal planning app.
        # He goes online to the meal planner's homepage.
        self.browser.get("http://localhost:8000")
        # He notices that "Home" is in the browser title.
        assert "Home" in self.browser.title
        self.assertIn("Home", self.browser.title)

        # He invited to create an account.
        self.fail("TODO: Finish the test!")

        # He types his name (David) into the Username box and pasword123 into the password box (David doesn't understand cybersecurity).

        # When he hits enter, he logs in and is redirected to his dashboard.

if __name__ == "__main__":
    unittest.main()
