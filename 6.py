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
time.sleep(5)

"""очищаем заполненное поле"""
user_name.clear()


# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input password")
#
# login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# login_button.click()
# print("Click login button")

time.sleep(5)
driver.close()

