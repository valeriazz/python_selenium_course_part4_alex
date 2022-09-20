import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)
# base_url = 'https://demoqa.com/elements'
# base_url = 'https://demoqa.com/radio-button'
# base_url = 'https://demoqa.com/buttons'
base_url = 'https://demoqa.com/date-picker'
# base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html' # запасной сайт
driver.get(base_url)
driver.maximize_window()

# elements = driver.find_element(By.XPATH, "//div[@class='card-body']/h5")
# time.sleep(5)
# elements.click()
# print('Click Elements')

# """работа с чекбоксами"""
# menu_check_box = driver.find_element(By.XPATH, "//ul[@class='menu-list']/li[@id='item-1']")
# menu_check_box.click()
# print('Click Menu-> Checkbox')
#
# check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
# check_box.click()
# print('Click Checkbox')
#
# check_button = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_button.click()
# print('Click Check button')

"""работа с радиокнопками"""
# menu_radio_button = driver.find_element(By.XPATH, "//li[@class='btn btn-light active' and @id='item-2']")
# menu_radio_button.click()

# print('Click Menu-> Radio-button')
# radio_button = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
# radio_button.click()
# print('Click Radio-button')

# """работа с кнопками"""
# action = ActionChains(driver)
# """двойной клик"""
# double_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# action.double_click(double_button).perform()
# print('Double click double-button')
#
# """нажатие правой кнопкой мыши"""
# right_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# action.context_click(right_button).perform()
# print('Right click button')

"""работа с календарём"""
"""1)ввод даты вручную"""
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
"""очищаем поле предварительно"""
# new_date.send_keys(Keys.BACKSPACE * 10)
# time.sleep(5)
# new_date.send_keys('09/17/2022')
time.sleep(5)
"""нажимаем enter"""
# new_date.send_keys(Keys.RETURN)
# print('Enter new date')
# time.sleep(5)

"""2)выбираем текущий день в календаре, обращаясь по XPATH к части класса"""
# new_day = driver.find_element(By.XPATH, "//div[@aria-label='Choose Saturday, September 17th, 2022']")
# new_day.click()
# today = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
# today.click()
# print('Today date')

"""3)выбираем месяц и день в календаре"""
# month_pick = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
# month_pick.click()
# month = driver.find_element(By.XPATH, "//option[@value='10']")
# month.click()
# day = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, November 1st, 2022']")
# day.click()
# print('Date is chosen')

"""4)как обратиться к любому нужному числу, например, сегодня 16.09, а хотим ввести 20.09"""
today = datetime.datetime.utcnow().strftime("%d")
today_day = int(today)
chosen_day = today_day + 4
locator = "//div[@aria-label='Choose Tuesday, September " + str(chosen_day) + "th, 2022']"
print(locator)
print('Date +4 is chosen')

chosen_date = driver.find_element(By.XPATH, locator)
chosen_date.click()



time.sleep(10)
driver.close()

