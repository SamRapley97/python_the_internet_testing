import pytest 
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBrokenImages:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/broken_images")
        yield
        self.driver.quit()
   

    def test_images_are_displaying(self):
        contentDiv = self.driver.find_element(By.CLASS_NAME, "example")
        images = contentDiv.find_elements(By.TAG_NAME, "img")
        for image in images:
            imageLink = image.get_attribute("src")
            r = requests.get(imageLink)
            if r.status_code != 200:
                print(imageLink + " is broken")
            else:
                print(imageLink + " is working")
