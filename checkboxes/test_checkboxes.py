import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckboxes:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        yield
        input("test")
        self.driver.quit()
   

    def test_check_first_box(self):
        contentDiv = self.driver.find_element(By.CLASS_NAME, "example")
        firstCheckbox = contentDiv.find_elements(By.TAG_NAME, "input")[0]
        firstCheckbox.click()
        assert firstCheckbox.is_selected() == True


        
