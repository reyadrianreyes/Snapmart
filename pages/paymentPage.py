from locators.locators import Locators

class PaymentPage():

    def __init__(self, driver):
        self.driver = driver

        self.card_payment_radiobutton_xpath = Locators.card_payment_radiobutton_xpath
        self.continue_button_xpath = Locators.payment_continue_button_xpath

    def select_card_payment(self):
        self.driver.find_element_by_xpath(self.card_payment_radiobutton_xpath).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()