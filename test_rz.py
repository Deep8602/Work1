from selenium import webdriver
import unittest

from TestRozetkaPO.RozetkaSerchPage import RozetkaSerchPage


class TestRozetka(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/d.popovych/PycharmProjects/WebDriver/chromedriver.exe")
        self.driver.get("https://rozetka.com.ua")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit

    def test_Search(self):
        rozetka = RozetkaSerchPage(self.driver)
        result = rozetka.search('apple iphone 7')
        assert "iPhone 7" in result.get_title_text()
