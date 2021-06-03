from selenium import webdriver
import pytest
from pages.landingPage import LandingPage
from pages.loginPage import LoginPage
from pages.shopPage import ShopPage
from pages.basketPage import BasketPage
from pages.addressPage import AddressPage
from pages.deliveryMethodPage import DeliveryMethodPage
from pages.paymentPage import PaymentPage
from pages.orderSummaryPage import OrderSummaryPage

@pytest.mark.usefixtures("test_setup")
class TestPlaceOrder():

    def test_go_to_login(self):
        driver = self.driver
        # Landing Page
        landing = LandingPage(driver)
        landing.go_to_application("https://test.cuongnguyen.online/#/")
        landing.click_dismiss()
        landing.click_account_navbar()
        landing.click_login_navbar()

        # Login Page
        login = LoginPage(driver)
        login.enter_username("reyadrianreyes+test@gmail.com")
        login.enter_password("test1234")
        login.click_login()

        # Shop Page
        shop = ShopPage(driver)
        shop.click_add_to_basket()
        shop.click_your_basket()

        # Basket Page
        basket = BasketPage(driver)
        basket.click_checkout()

        # Address Page
        address = AddressPage(driver)
        address.select_address()
        address.click_continue()

        # Delivery Method Page
        delivery = DeliveryMethodPage(driver)
        delivery.select_one_day_delivery()
        delivery.click_continue()

        # Payment Page
        payment = PaymentPage(driver)
        payment.select_card_payment()
        payment.click_continue()

        # Order Summary
        order = OrderSummaryPage(driver)
        order.check_items_price()
        order.check_delivery_price()
        order.check_promotion_price()
        order.check_total_price()
        order.click_checkout()

