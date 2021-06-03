import time
from locators.locators import Locators

class AddressPage():

    def __init__(self, driver):
        self.driver = driver

        self.address_radiobutton_xpath = Locators.address_radiobutton_xpath
        self.continue_button_xpath = Locators.address_continue_button_xpath

    def select_address(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.address_radiobutton_xpath).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()
