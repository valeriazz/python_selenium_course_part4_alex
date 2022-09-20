import time
from selenium import webdriver

"""2 вариант (в отличие от chrome) для определения пути, где лежит geckodriver.exe:"""
driver = webdriver.Firefox(executable_path='C:\\pythonSelenium\\geckodriver.exe')

"""запускаем браузер:"""
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(5)
driver.close()


