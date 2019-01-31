import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from BaseTest import BaseTest
from RozetkaSerchPage import RozetkaSerchPage


class TestRozetka(BaseTest):

    def test_search(self):
        rozetka = RozetkaSerchPage()
        time.sleep(2)
        rozetka.push(rozetka.search_input_loc)
        rozetka.write_on_field('apple iphone 7', rozetka.search_input_loc)
        rozetka.push(rozetka.search_btn_loc)
        assert "iPhone" in rozetka.driver.title, \
            ''' Check the search on first page '''

        rozetka.select_goods(rozetka.list_of_goods_loc, 2)
        rozetka.back_to_privies_page(rozetka.buy_btn_loc)
        rozetka.push(rozetka.buy_btn_loc)
        rozetka.push(rozetka.order_btn_loc)
        rozetka.write_on_field('param pam pam', rozetka.name_fiald_loc)
        rozetka.clear_input(rozetka.city_fiald_loc)
        rozetka.select_in_drop_down(rozetka.city_drop_down_loc, 'Львов')
        time.sleep(5)
        rozetka.write_on_field('Винница', rozetka.city_fiald_loc)
        rozetka.write_on_field('0637000000', rozetka.phone_fiald_loc)
        rozetka.write_on_field("somemail@gmail.com", rozetka.mail_fiald_loc)
        time.sleep(5)
        rozetka.push(rozetka.next_btn_loc)
