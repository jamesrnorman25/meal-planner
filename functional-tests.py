from selenium import webdriver

# Server test
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Congratulations" in browser.title
