import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)

base_url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(base_url)
driver.maximize_window()

"""Работа с ползунком (в move_by_offset(X, Y) - тянем по горизонтали/вертикали), release - отпускаем мышь, 
perform - сохраняет наше действие"""
action = ActionChains(driver)
price = driver.find_element(By.XPATH, "//div[@id='layered_price_slider']")
action.click_and_hold(price).move_by_offset(20, 0).release().perform()
print('Price +')


time.sleep(10)
driver.close()
