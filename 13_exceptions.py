import datetime
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)

# base_url = 'https://demoqa.com/dynamic-properties'
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

"""работа с исключениями"""
"""dynamic-properties"""
# try:
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print('NoSuchElementException exception')
#     time.sleep(10)
#     driver.refresh()
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
#     print('Click visible button')

"""radio-button"""
yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_button.click()
try:
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    time.sleep(5)
    yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_button.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('Checkbox YES')
print('Test is over')

time.sleep(10)
driver.close()

