import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('C:\\pythonSelenium\\chromedriver.exe')

driver = webdriver.Chrome(service=s)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

"""new date +10days'"""
now_date = datetime.datetime.utcnow().strftime("%m/%d/%Y")
print(now_date)
list_date = now_date.split('/')
month = list_date[0]
year = list_date[2]
new_day = int(list_date[1]) + 10

# високосный год
if month == '02' and new_day > 29 and ((int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0):
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 29)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
else: # невисокосный год
    if month == '02' and new_day > 28:
        month = ''.join('0') + str(int(list_date[0]) + 1)
        new_day = int(new_day - 28)
        if 1 < new_day < 10:
            new_day = ''.join('0') + str(new_day)
if month in ('01', '03', '05', '07', '08') and int(new_day) > 31:
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month == '10' and new_day > 31:
    month = str(int(list_date[0]) + 1)
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month == '12' and new_day > 31:
    month = '01'
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
    year = int(year) + 1
elif month in ('04', '06') and new_day > 30:
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 30)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month in ('09', '11') and new_day > 30:
    month = int(list_date[0]) + 1
    new_day = int(new_day - 30)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
new_date = ''.join(str(month) + '/' + str(new_day) + '/' + str(year))
print(new_date)


"""input new date into date_field"""
date_field = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_field.click()
date_field.send_keys(Keys.BACKSPACE * 10)
time.sleep(5)
date_field.send_keys(new_date)
date_field.send_keys(Keys.RETURN)
print("Input +10days' date")

"""assertion"""
assert date_field.get_attribute('value') == new_date
print('Date is correct')


# """Заполнение второго поля датой +10 (формат September 27, 2022 9:15 AM) без участия локатора"""
# БЕЗ ПРОВЕРОК ПО МЕСЯЦАМ, КАК ВЫШЕ!!! ДОПИСАТЬ ПОТОМ
#
# """new_date +10days'"""
# now_date_2 = datetime.datetime.utcnow().strftime("%B %d, %Y %H:%M %p")
# print(now_date_2)
# list_date_2 = now_date_2.split(',')[0]
# list_date_2_1 = now_date_2.split(',')[1]
# month = list_date_2.split(' ')[0]
# day = list_date_2.split(' ')[1]
# new_day_2 = int(day) + 10
# new_date_2 = ''.join(month + ' ' + str(new_day_2) + ',' + list_date_2_1)
# print(new_date_2)
#
# """input new date into date_field"""
# """второе поле ну очень криво очищается, помог только костыль ниже с backspace+delete)))"""
# date_field_2 = driver.find_element(By.XPATH, "//input[@id='dateAndTimePickerInput']")
# date_field_2.click()
# date_field_2.send_keys(Keys.BACKSPACE * 11)
# date_field_2.send_keys(Keys.DELETE * 16)
# time.sleep(5)
# date_field_2.send_keys(new_date_2)
# date_field_2.send_keys(Keys.RETURN)
# print("Input_2 +10days' date")
# print(str(date_field_2.get_attribute('value')))
# print(str(new_date_2))
#
# """assertion: здесь выяснилось, что в dom-дереве в атрибуте value час указывается без 0! Поэтому для проверки
# часов, начинающихся с 0 (00-09) пришлось ниже сделать костыль"""
#
# hour_minute = new_date_2.split(' ')[3]
# hour = hour_minute.split(':')[0]
# minute = hour_minute.split(':')[1]
# print(hour)
# if int(hour) < 10:
#     new_hour = list(hour)[1]
#     print(new_hour)
#     new_date_2_hour = ''.join(new_date_2.split(' ')[0] + ' ' + new_date_2.split(' ')[1] + ' ' + new_date_2.split(' ')[2]
#                           + ' ' + str(new_hour) + ':' + str(minute) + ' ' + new_date_2.split(' ')[4])
#     print(new_date_2_hour)
#     assert date_field_2.get_attribute('value') == new_date_2_hour
#     print('Date is correct')
# else:
#     assert date_field_2.get_attribute('value') == new_date_2
#     print('Date is correct')

time.sleep(10)
driver.close()
