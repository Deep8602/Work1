import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from utilities.DriverWrapper import DriverWrapper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    wait_element_time = 10

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)
        self.driver.maximize_window()

    def write_on_field(self, param, locator_field):
        input_field = self.wait.until(EC.presence_of_element_located(locator_field), 'There is no input')
        input_field.send_keys(param)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)
        return self

    def push(self, element_locator, error='This item is not clickable'):
        """ Wait for the expected item and clicks on it """
        element = self.wait.until(EC.presence_of_element_located(element_locator), error)
        element.click()
        return self

    def select_goods(self, element_locator, num):
        list_of_goods = self.wait.until(EC.presence_of_all_elements_located(element_locator))
        goods_num = list_of_goods.pop(num)
        goods_num.click()
        return self

    def back_to_privies_page(self, element_locator, error="The item what you are looking for, was not found."):
        """ Wait element on page until element to by presence
            if expected element not found returns to the previous page """
        try:
            self.wait.until(EC.presence_of_element_located(element_locator), error)
            return True
        except:
            self.driver.back()

    def clear_input(self, input_locator):
        """ Allocates and removes everything in input """
        input_field = self.wait.until(EC.presence_of_element_located(input_locator))
        (input_field.send_keys(Keys.CONTROL + "a"))
        (input_field.send_keys(Keys.DELETE))
        (input_field.send_keys(Keys.ENTER))
        return self

    def select_in_drop_down(self, input_loc, text):
        drop_down = self.wait.until(EC.presence_of_all_elements_located(input_loc))
        print(drop_down)
        for select in drop_down:
            if select.text == text:
                return select.click()



