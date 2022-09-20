import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

"""явные и неявные ожидания: вместе их использовать нельзя для всех тестов, будут конфликты"""
"""неявное ожидание - применяется ко всем действиям тестов одинаково"""
# driver.implicitly_wait(10)

"""явное ожидание - применяется к конкретному действию в тесте, когда будет кликабельным какой-то элемент итд. Более 
надёжный и стабильный способ, чем implicitly_wait"""

print('Start Test')
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print('Finish Test')


# print('Start Test')
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print('Finish Test')


time.sleep(10)
driver.close()

