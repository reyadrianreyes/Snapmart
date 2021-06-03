import time
from locators.locators import Locators

class DeliveryMethodPage():

    def __init__(self, driver):
        self.driver = driver

        self.one_day_delivery_radiobutton_xpath = Locators.one_day_delivery_radiobutton_xpath
        self.continue_button_xpath = Locators.delivery_continue_button_xpath

    def select_one_day_delivery(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.one_day_delivery_radiobutton_xpath).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()
