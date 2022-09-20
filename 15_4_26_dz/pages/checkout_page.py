import datetime
import time
from .page import Page
from .locators import CheckoutPageLocators

fn = 'Valeria'
ls = 'Zlenko'
pc = '123321'

class CheckoutPage(Page):
    def do_checkout(self):
        first_name = self.browser.find_element(*CheckoutPageLocators.first_name)
        first_name.send_keys(fn)
        print('First name')
        last_name = self.browser.find_element(*CheckoutPageLocators.last_name)
        last_name.send_keys(ls)
        print('Last name')
        postal_code = self.browser.find_element(*CheckoutPageLocators.postal_code)
        postal_code.send_keys(pc)
        print('Zip')

    def go_to_overview_page(self):
        continue_button = self.browser.find_element(*CheckoutPageLocators.continue_button)
        continue_button.click()
        print('Go to Overview page')

    def make_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot-' + now_date + '.png'
        self.browser.save_screenshot('.\\screen\\' + name_screenshot)
        print('Screen is made successfully')


