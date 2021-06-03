import time
from locators.locators import Locators

class OrderSummaryPage():

    def __init__(self, driver):
        self.driver = driver

        self.items_text = Locators.items_text
        self.delivery_text = Locators.delivery_text
        self.promotion_text = Locators.promotion_text
        self.total_text = Locators.total_text
        self.place_your_order_and_pay_button_id = Locators.place_your_order_and_pay_button_id

    def check_items_price(self):
        time.sleep(2)
        items = self.driver.find_element_by_xpath(self.items_text).text
        print(items)
        assert items == "1.99¤"
        # Need to improve assertion here.

    def check_delivery_price(self):
        delivery = self.driver.find_element_by_xpath(self.delivery_text).text
        print(delivery)
        assert delivery == "0.99¤"
        # Need to improve assertion here.

    def check_promotion_price(self):
        promotion = self.driver.find_element_by_xpath(self.promotion_text).text
        print(promotion)
        assert promotion == "0.00¤"
        # Need to improve assertion here.

    def check_total_price(self):
        total = self.driver.find_element_by_xpath(self.total_text).text
        print(total)
        assert total == "2.98¤"
        # Need to improve assertion here.

    def click_checkout(self):
        self.driver.find_element_by_id(self.place_your_order_and_pay_button_id).click()
