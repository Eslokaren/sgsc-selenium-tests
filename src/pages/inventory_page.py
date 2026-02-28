from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text
