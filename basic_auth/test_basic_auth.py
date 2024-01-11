import pytest 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddRemoveElement:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        yield
        self.driver.quit()
   

    def test_login_credentials_are_correct(self):
        contentDiv = self.driver.find_element(By.CLASS_NAME, "example")
        pageText = contentDiv.find_element(By.TAG_NAME, "p").text
        assert pageText == "Congratulations! You must have the proper credentials."


        


