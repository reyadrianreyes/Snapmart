import time
from locators.locators import Locators

class BasketPage():

    def __init__(self, driver):
        self.driver = driver

        self.checkout_button_id = Locators.checkout_button_id

    def click_checkout(self):
        time.sleep(2)
        self.driver.refresh()
        self.driver.find_element_by_id(self.checkout_button_id).click()
