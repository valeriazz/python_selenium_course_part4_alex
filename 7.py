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

"""работа со скрытым меню"""
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
print("Click menu button")

about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
about.click()
print("Click about button")

"""нажать на назад в браузере"""
driver.back()
print('Go Back')
time.sleep(10)
driver.forward()
print('Go Forward')

time.sleep(10)
driver.close()

