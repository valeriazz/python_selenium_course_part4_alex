import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

"""инициализируем браузер"""
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""выносим отдельно переменные логина и пароля"""
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

"""вводим логин"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")

"""вводим пароль"""
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")

"""нажимаем на кнопку логина"""
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click login button")

"""при введении некорректного логина/пароля есть предупреждение, проверяем, что оно имеется"""
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print('Warning')

"""обновляем страницу"""
driver.refresh()

time.sleep(5)
driver.close()

