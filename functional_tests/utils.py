from selenium.common.exceptions import WebDriverException
import time

def wait_for(function, max, step):
    """Taken from book 'Obey the Testing Goat' by Harry Percival"""
    start_time = time.time()
    while True:
        try:
            return function()  
        except (AssertionError, WebDriverException):
            if time.time() - start_time > max:
                raise
            time.sleep(step)