import datetime
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

time.sleep(5)

"""делаем скриншот"""
"""чтобы название было актуальным, можно задать дату для скриншота"""
# now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
name_screenshot = 'screenshot-' + now_date + '.png'
"""путь до папки screen"""
driver.save_screenshot('.\\screen\\' + name_screenshot)


time.sleep(5)
driver.close()

