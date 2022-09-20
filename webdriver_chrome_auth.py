import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""для определения пути, где лежит chromedriver.exe:"""
from selenium.webdriver.chrome.service import Service
"""передаем в webdriver.Chrome экземпляр импортированного класса Service, чтобы инициализировать chromedriver.exe:"""
s = Service('C:\\pythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

"""запускаем браузер:"""
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# Авторизация

"""ищем поле логина (разными методами)"""
# user_name = driver.find_element(By.ID, 'user_name') #ID
# user_name = driver.find_element(By.NAME, 'user_name') #NAME
# user_name = driver.find_element(By.XPATH, "//*[@id='user-name']") #XPATH
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #ID XPATH
# user_name = driver.find_element(By.XPATH, "//input[@data-test='username']") #DATA-TEST XPATH

"""заполняем поле значением"""
user_name.send_keys('standard_user')

"""ищем поле пароля"""
password = driver.find_element(By.CSS_SELECTOR, '#password') #ID CSS SELECTOR
"""заполняем поле значением"""
password.send_keys('secret_sauce')

"""ищем кнопку логина"""
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
"""нажимаем на кнопку логина"""
login_button.click()

"""на главной странице проверяем, что текст на кнопке Products совпадает"""
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text  # cчитываем текст с элемента
print(value_text_products)


time.sleep(5)
driver.close()
