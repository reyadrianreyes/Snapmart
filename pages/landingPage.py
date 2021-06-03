from locators.locators import Locators

class LandingPage():

    def __init__(self, driver):
        self.driver = driver

        self.dismiss_button_xpath = Locators.dismiss_button_xpath
        self.account_button_id = Locators.account_button_id
        self.login_navbar_button_id = Locators.login_navbar_button_id


    def go_to_application(self, URL):
        self.driver.get(URL)

    def click_dismiss(self):
        self.driver.find_element_by_xpath(self.dismiss_button_xpath).click()

    def click_account_navbar(self):
        self.driver.find_element_by_id(self.account_button_id).click()

    def click_login_navbar(self):
        self.driver.find_element_by_id(self.login_navbar_button_id).click()