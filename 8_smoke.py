import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click login button")

"""INFO Product 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select Product 1')

basket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
basket.click()
print('Go Basket')

"""INFO Product 1 in Basket"""
basket_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_basket_product_1 = basket_product_1.text
print(value_basket_product_1)
assert value_product_1 == value_basket_product_1
print('Product 1 is the same')

basket_price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_basket_price_product_1 = basket_price_product_1.text
print(value_basket_price_product_1)
assert value_price_product_1 == value_basket_price_product_1
print('Price of Product 1 is the same')

"""переход на страницу оформления заказа"""
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()

"""User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Valeria')
print('First name')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Zlenko')
print('Last name')
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('111111')
print('Zip')

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Go Overview')

"""INFO Overview Product 1"""
overview_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_overview_product_1 = overview_product_1.text
print(value_overview_product_1)
assert value_product_1 == value_overview_product_1
print('OK!')

overview_price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_overview_price_product_1 = overview_price_product_1.text
print(value_overview_price_product_1)
assert value_price_product_1 == value_overview_price_product_1
print('OK!')

overview_price_product_1_final = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_overview_price_product_1_final = overview_price_product_1_final.text
print(value_overview_price_product_1_final)
assert value_price_product_1 in value_overview_price_product_1_final
print('OK!')


time.sleep(10)
driver.close()

