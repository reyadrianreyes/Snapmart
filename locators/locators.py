class Locators():
    # Landing Page
    dismiss_button_xpath = "//span[contains(text(),'Dismiss')]"
    account_button_id = "navbarAccount"
    login_navbar_button_id = "navbarLoginButton"

    # Login Page
    username_textbox_id = "email"
    password_textbox_id = "password"
    login_button_id = "loginButton"

    # Shop Page
    AddToBasket_button_xpath = "//span[contains(text(),'Add to Basket')]"
    YourBasket_button_xpath = "//span[contains(text(),'Your Basket')]"

    # Basket Page
    checkout_button_id = "checkoutButton"

    # Address Page
    address_radiobutton_xpath = "//mat-cell[contains(text(),'Test, Test, Test, 1012')]"
    address_continue_button_xpath = "//span[contains(text(),'Continue')]"

    # Delivery Method Page
    one_day_delivery_radiobutton_xpath = "//mat-cell[contains(text(),'1 Days')]"
    delivery_continue_button_xpath = "//span[contains(text(),'Continue')]"

    # Payment Page
    card_payment_radiobutton_xpath = "//span[@class='mat-radio-container']"
    payment_continue_button_xpath = "//span[contains(text(),'Continue')]"

    # Order Summary
    items_text = "//mat-card[1]/table[1]/tr[1]/td[2]"
    delivery_text = "//mat-card[1]/table[1]/tr[2]/td[2]"
    promotion_text = "//mat-card[1]/table[1]/tr[3]/td[2]"
    total_text = "//mat-card[1]/table[1]/tr[4]/td[2]"
    place_your_order_and_pay_button_id = "checkoutButton"
