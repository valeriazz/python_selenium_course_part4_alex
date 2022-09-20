import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service('C:\\pythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()


"""Authorization"""
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print('Click login button')


"""INFO Product 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_1 = product_1.text
print('Name of Product 1: ' + str(value_product_1))

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print('Price of Product 1: ' + str(value_price_product_1))

"""Add Product 1 to Basket"""
add_button_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
add_button_product_1.click()
print('Add Product 1 to basket')


"""INFO Product 2"""
product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_product_2 = product_2.text
print('Name of Product 2: ' + str(value_product_2))

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print('Price of Product 2: ' + str(value_price_product_2))

"""Add Product 2 to Basket"""
add_button_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
add_button_product_2.click()
print('Add Product 2 to basket')


"""Go to Basket"""
basket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
basket.click()
print('Go to Basket')


"""INFO Product 1 in Basket"""
basket_product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_basket_product_1 = basket_product_1.text
print('Name of Product 1 in Basket: ' + str(value_basket_product_1))
assert value_basket_product_1 == value_product_1
print('OK, Product 1 is the same!')

basket_price_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_basket_price_product_1 = basket_price_product_1.text
print('Price of Product 1 in Basket: ' + str(value_basket_price_product_1))
assert value_basket_price_product_1 == value_price_product_1
print('OK, Product 1 price is the same!')


"""INFO Product 2 in Basket"""
basket_product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_basket_product_2 = basket_product_2.text
print('Name of Product 2 in Basket: ' + str(value_basket_product_2))
assert value_basket_product_2 == value_product_2
print('OK, Product 2 is the same!')

basket_price_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_basket_price_product_2 = basket_price_product_2.text
print('Price of Product 2 in Basket: ' + str(value_basket_price_product_2))
assert value_basket_price_product_2 == value_price_product_2
print('OK, Product 2 price is the same!')

"""Go to UserData page"""
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Go to UserData page')

"""Checkout"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Valeria')
print('First name')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Zlenko')
print('Last name')
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('111111')
print('Zip')

"""Go to Overview page"""
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Go to Overview page')

time.sleep(10)

"""Make screenshot"""
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot-' + now_date + '.png'
driver.save_screenshot('.\\screen\\' + name_screenshot)
print('Screen is made successfully')


"""INFO Overview Product 1"""
overview_product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_overview_product_1 = overview_product_1.text
print('Final Name of Product 1: ' + str(value_overview_product_1))
assert value_product_1 == value_overview_product_1
print('OK, Final Name of Product 1 is correct')

overview_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_overview_price_product_1 = overview_price_product_1.text
print('Final Price of Product 1: ' + str(value_overview_price_product_1))
assert value_price_product_1 == value_overview_price_product_1
print('OK, Final Price of Product 1 is correct')


"""INFO Overview Product 2"""
overview_product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_overview_product_2 = overview_product_2.text
print('Final Name of Product 2: ' + str(value_overview_product_2))
assert value_product_2 == value_overview_product_2
print('OK, Final Name of Product 2 is correct')

overview_price_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_overview_price_product_2 = overview_price_product_2.text
print('Final Price of Product 2: ' + str(value_overview_price_product_2))
assert value_price_product_2 == value_overview_price_product_2
print('OK, Final Price of Product 2 is correct')


"""Total sum without $"""
total_sum = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_total_sum = str(total_sum.text).replace('Item total: $', '')
print('Total Sum is ' + value_total_sum)

"""Counting sums of two products"""
sum_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_sum_product_1 = str(sum_product_1.text).replace('$', '')
print(value_sum_product_1)
sum_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_sum_product_2 = str(sum_product_2.text).replace('$', '')
print(value_sum_product_2)

count_sum = float(value_sum_product_1) + float(value_sum_product_2)
print('Counted sum of two products is: ' + str(count_sum))

assert float(count_sum) == float(value_total_sum)
print('The system counted total sum correctly!!!')

time.sleep(10)
driver.close()


