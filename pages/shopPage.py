import time
from locators.locators import Locators

class ShopPage():

    def __init__(self, driver):
        self.driver = driver

        self.AddToBasket_button_xpath = Locators.AddToBasket_button_xpath
        self.YourBasket_button_xpath = Locators.YourBasket_button_xpath

    def click_add_to_basket(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.AddToBasket_button_xpath).click()

    def click_your_basket(self):
        self.driver.find_element_by_xpath(self.YourBasket_button_xpath).click()

