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
        self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        self.buttonDiv = self.driver.find_element(By.CLASS_NAME, "example")
        self.button = self.buttonDiv.find_element(By.XPATH, "//button[.='Add Element']")
        yield
        self.driver.quit()
   

    def test_site_title_is_correct(self):
        assert self.driver.title == "The Internet"

    def test_button_adds_element(self):
        self.button.click()
        deleteButton = self.driver.find_element(By.CLASS_NAME, "added-manually")
        assert deleteButton.is_displayed()
     

    def test_button_deletes_element(self):
        self.button.click()
        deleteButton = self.driver.find_element(By.CLASS_NAME, "added-manually")
        deleteButton.click()
        assert WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((deleteButton)))
     




