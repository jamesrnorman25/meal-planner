import os
import unittest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from .utils import wait_for

from mealplan.models import Mealplan


MAX_WAIT = 3  # Max wait for browser load.
WAIT_STEP = 0.5  # Wait step for browser load.


class NewVisitorTest(StaticLiveServerTestCase):
    username = "David"
    password = "i@N7bR4ASnL0q$"
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = f"http://{test_server}"

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
        
        wait_for(lambda: self.assertIn("Create Account", self.browser.title), MAX_WAIT, WAIT_STEP)

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
        wait_for(lambda: self.assertIn(f"Dashboard - {self.username}", self.browser.title), MAX_WAIT, WAIT_STEP)

        # Satisfied, he clicks on the log out button and is redirected back to the homepage.
        logout_button = self.browser. find_element(By.ID, "id_link_logout")
        logout_button.click()
        wait_for(lambda: self.assertIn("Home", self.browser.title), MAX_WAIT, WAIT_STEP)


class ExistingUserLoginTest(StaticLiveServerTestCase):
    username = "David"
    password = "password123"

    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = f"http://{test_server}"

    
    def tearDown(self) -> None:
        self.browser.close()
        User.objects.filter(username=self.username).delete()

    def test_user_can_log_in(self) -> None:
        # After a while, David wants to return to the website.
        self.browser.get(self.live_server_url)
        # He clicks on the log in link in the navbar and is directed to the login page.
        login_link = self.browser.find_element(By.ID, "id_link_login")
        login_link.click()
        
        wait_for(lambda: self.assertIn("Login", self.browser.title), MAX_WAIT, WAIT_STEP)
        
        # David types his username and password into the required boxes and hits Enter
        username_box = self.browser.find_element(By.ID, "id_username")
        password_box = self.browser.find_element(By.ID, "id_password")
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)

        # As before, he is redirected to his dashboard.
        wait_for(lambda: self.assertIn(f"Dashboard - {self.username}", self.browser.title), MAX_WAIT, WAIT_STEP)
        

class NewMealplanTest(StaticLiveServerTestCase):
    username = "David"
    password = "password123"

    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        cookie = self.client.cookies["sessionid"]
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = f"http://{test_server}"
        self.browser.get(self.live_server_url)
        self.browser.add_cookie({"name": "sessionid", "value": cookie.value, "secure": False, "path": '/'})
        self.browser.refresh()


    
    def tearDown(self) -> None:
        self.browser.close()
        User.objects.filter(username=self.username).delete()

    def test_user_can_create_mealplans(self) -> None:
        # David logs in and goes to his dashboard.
        self.browser.get(f"{self.live_server_url}/Dashboard")
        self.assertIn(self.username, self.browser.title)

        # He clicks on the button to add a new weekly mealplan.
        mealplan_button = self.browser.find_element(By.ID, "id_link_new_mealplan")
        mealplan_button.click()

        # He is directed to a mealplan creation page.
        wait_for(lambda: self.assertEqual("New meal plan", self.browser.title), MAX_WAIT, WAIT_STEP)

        # He types the following mealplan into the boxes, with the title "Next Week" before clicking "Save"
        # Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
        # ------ | ------- | --------- | -------- | ------ | -------- | ------
        # Salad  | Chicken | Spag bol  | Fajitas  | Salmon |   Stew   | Roast

        name_box = self.browser.find_element(By.ID, "id_name")
        name_box.send_keys("Next Week")
        monday_box = self.browser.find_element(By.ID, "id_monday")
        monday_box.send_keys("Salad")
        tuesday_box = self.browser.find_element(By.ID, "id_tuesday")
        tuesday_box.send_keys("Chicken")
        wednesday_box = self.browser.find_element(By.ID, "id_wednesday")
        wednesday_box.send_keys("Spag bol")
        thursday_box = self.browser.find_element(By.ID, "id_thursday")
        thursday_box.send_keys("Fajitas")
        friday_box = self.browser.find_element(By.ID, "id_friday")
        friday_box.send_keys("Salmon")
        saturday_box = self.browser.find_element(By.ID, "id_saturday")
        saturday_box.send_keys("Stew")
        sunday_box = self.browser.find_element(By.ID, "id_sunday")
        sunday_box.send_keys("Roast")
        submit_box = self.browser.find_element(By.ID, "id_submit")
        self.assertEqual(submit_box.text, "Save")
        submit_box.click()
        

        # He sees that he has been redirected to a page with a different URL displaying the mealplan.
        wait_for(lambda: self.assertNotEqual(f"{self.live_server_url}/mealplans/new", self.browser.current_url), MAX_WAIT, WAIT_STEP)
        self.assertIn("Next Week", self.browser.find_element(By.TAG_NAME, "h1").text)
        
        # Finally, he returns to his dashboard to see his mealplan displayed there.
        self.browser.find_element(By.ID, "id_link_dashboard").click()
        wait_for(lambda: self.assertEqual("Next Week", self.browser.find_element(By.NAME, "header-next-week").text), MAX_WAIT, WAIT_STEP)

class ExistingMealplanTest(StaticLiveServerTestCase):
    username = "David"
    password = "password123"
    mealplan_data = {"name": "Next week", "monday": "Salad", "tuesday": "Chicken",
                     "wednesday": "Spag bol", "thursday": "Fajitas", "friday": "Salmon",
                     "saturday": "Stew", "sunday": "Roast"}

    def setUp(self) -> None:
        user = User.objects.create_user(username=self.username, password=self.password, is_active=1)
        user.save()
        self.client.force_login(user=user)
        mealplan = Mealplan.objects.create(**self.mealplan_data)
        mealplan.user = user
        mealplan.save()
        cookie = self.client.cookies["sessionid"]
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = f"http://{test_server}"
        self.browser.add_cookie({"name": "sessionid", "value": cookie.value, "secure": False, "path": '/'})
        self.browser.refresh()

    def tearDown(self):
        self.browser.close()
        User.objects.filter(username=self.username).delete()
        Mealplan.objects.filter(name=self.mealplan_data["name"]).delete()

    def test_user_can_edit_mealplans(self)-> None:
        # David has realised he needs to change his set mealplan for next week.
        # He navigates to his dashboard.
        self.browser.get(f"{self.live_server_url}/Dashboard")
        # He clicks on the "Edit Menu" button under his mealplan for the week.
        edit_button = self.browser.find_element(By.NAME, "link-edit-next-week")
        edit_button.click()

        # He is now taken to the mealplan's edit option.
        wait_for(lambda: self.assertIn("Edit Mealplan", self.browser.title), MAX_WAIT, WAIT_STEP)
        # He changes Monday's meal to "Leftovers" and clicks "Save".
        monday_input = self.browser.find_element(By.ID, "id_monday")
        monday_input.clear()
        monday_input.send_keys("Leftovers")
        self.browser.find_element(By.ID, "id_submit").click()
        # He is then redirected to the page for the mealplan and notices that it now displays "Leftovers" for Monday's meal..
        wait_for(lambda: self.assertIn("Next week".upper(), self.browser.title.upper()), MAX_WAIT, WAIT_STEP)
        monday = self.browser.find_element(By.ID, "id_monday")
        self.assertIn("Leftovers", monday.text)


if __name__ == "__main__":
    unittest.main()
