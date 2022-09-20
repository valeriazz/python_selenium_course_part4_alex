from selenium.webdriver.common.by import By


class LoginPageLocators():
    user_name = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")


class ProductPageLocators():
    product_1 = (By.XPATH, "//a[@id='item_4_title_link']")
    price_product_1 = (By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
    add_button_product_1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    product_2 = (By.XPATH, "//a[@id='item_0_title_link']")
    price_product_2 = (By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
    add_button_product_2 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")

    product_3 = (By.XPATH, "//a[@id='item_1_title_link']")
    price_product_3 = (By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    add_button_product_3 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")

    product_4 = (By.XPATH, "//a[@id='item_5_title_link']")
    price_product_4 = (By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    add_button_product_4 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")

    product_5 = (By.XPATH, "//a[@id='item_2_title_link']")
    price_product_5 = (By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    add_button_product_5 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")

    product_6 = (By.XPATH, "//a[@id='item_3_title_link']")
    price_product_6 = (By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
    add_button_product_6 = (By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    cart_link = (By.XPATH, "//a[@class='shopping_cart_link']")


class CartPageLocators():
    cart_product_1 = (By.XPATH, "//a[@id='item_4_title_link']")
    cart_price_product_1 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    cart_product_2 = (By.XPATH, "//a[@id='item_0_title_link']")
    cart_price_product_2 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    cart_product_3 = (By.XPATH, "//a[@id='item_1_title_link']")
    cart_price_product_3 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    cart_product_4 = (By.XPATH, "//a[@id='item_5_title_link']")
    cart_price_product_4 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    cart_product_5 = (By.XPATH, "//a[@id='item_2_title_link']")
    cart_price_product_5 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    cart_product_6 = (By.XPATH, "//a[@id='item_3_title_link']")
    cart_price_product_6 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    checkout = (By.XPATH, "//button[@id='checkout']")


class CheckoutPageLocators():
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")

    continue_button = (By.XPATH, "//input[@id='continue']")



class OverviewPageLocators():
    overview_product_1 = (By.XPATH, "//a[@id='item_4_title_link']")
    overview_price_product_1 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    overview_product_2 = (By.XPATH, "//a[@id='item_0_title_link']")
    overview_price_product_2 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    overview_product_3 = (By.XPATH, "//a[@id='item_1_title_link']")
    overview_price_product_3 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    overview_product_4 = (By.XPATH, "//a[@id='item_5_title_link']")
    overview_price_product_4 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    overview_product_5 = (By.XPATH, "//a[@id='item_2_title_link']")
    overview_price_product_5 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    overview_product_6 = (By.XPATH, "//a[@id='item_3_title_link']")
    overview_price_product_6 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    total_sum = (By.XPATH, "//div[@class='summary_subtotal_label']")


