from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage


class RozetkaSerchPage(BasePage):

    goods_locator = (By.CSS_SELECTOR, 'div.cat-g-b.clearfix div.g-i-tile-i-title.clearfix a')
    search_input_loc = (By.CSS_SELECTOR, 'input.rz-header-search-input-text.passive')
    search_btn_loc = (By.CSS_SELECTOR, 'button.btn-link-i.js-rz-search-button')
    buy_btn_loc = (By.CSS_SELECTOR, 'div.toOrder button.btn-link-i')
    order_btn_loc = (By.CSS_SELECTOR, 'button#popup-checkout')
    name_fiald_loc = (By.CSS_SELECTOR, '#reciever_name')
    list_of_goods_loc = (
        By.CSS_SELECTOR, 'div.g-i-tile-l.g-i-tile-catalog-hover-left-side.clearfix div.g-i-tile-i-title.clearfix a')
    city_fiald_loc = (By.CSS_SELECTOR, 'input.input-text.check-suggest-input-text.check-input-text')
    phone_fiald_loc = (By.CSS_SELECTOR, 'input.input-text.check-phone-input-full-text.check-input-text')
    mail_fiald_loc = (By.CSS_SELECTOR, 'input#reciever_email')
    next_btn_loc = (By.CSS_SELECTOR, 'div.check-f-i-field button.btn-link-i')
    city_drop_down_loc = (By.CSS_SELECTOR, 'div.dropdown-input li.suggestion-i')


#     def get_title_text(self):
#         print(self.driver.title)
#         return str(self.driver.title)
#
#     def get_goods(self, element_locator, numb_of_goods):
#         goods = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(element_locator))
#         one_goods = goods[numb_of_goods]
#         one_goods.click()
# #         return Buy_page()
#
#
# class Buy_page(RozetkaSerchPage):
#     button_bay_locator = (By.CSS_SELECTOR, 'div.toOrder button.btn-link-i')
#     pass
