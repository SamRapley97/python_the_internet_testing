import pytest 


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestContextMenu:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/context_menu")
        yield
        self.driver.quit()
   

    def test_right_click(self):
        action =  ActionChains(self.driver)
        contentDiv = self.driver.find_element(By.CLASS_NAME, "example")
        hotSpot = contentDiv.find_element(By.ID, "hot-spot")
        action.move_to_element(hotSpot).perform()
        action.context_click(hotSpot).perform()
        alert = self.driver.switch_to.alert
        assert alert.text == "You selected a context menu"

        