import time
from selenium import webdriver
from selenium.webdriver import Keys
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

# time.sleep(3)
#
# """стираем последний символ введенного логина"""
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# """после предыдущего удаления 2 символов мы снова их допишем"""
# user_name.send_keys('er')
# time.sleep(3)
# """удаляем сразу 5 символов"""
# user_name.send_keys(Keys.BACKSPACE * 5)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")
"""команда, чтобы залогиниться не через кнопку логина, а через Enter"""
password.send_keys(Keys.ENTER)

#
# login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
# login_button.click()
# print("Click login button")

"""после перехода на главную страницу работаем с фильтром"""
filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
print('Click Filter')
time.sleep(3)
"""опускаемся в фильтре на 1 строку в списке и нажимаем на Enter, чтобы активировать фильтр"""
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)

"""опускаемся в фильтре вниз списка и нажимаем на Enter, чтобы активировать фильтр"""
filter.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)


time.sleep(5)
driver.close()

