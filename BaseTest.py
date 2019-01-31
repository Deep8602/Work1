from selenium import webdriver
import pytest
from utilities.DriverWrapper import DriverWrapper


@pytest.mark.usefixtures('get_browser_name')
@pytest.mark.usefixtures('get_base_url')
@pytest.mark.usefixtures('get_base_host')

class BaseTest(object):

    def setup(self):

        self.driver = DriverWrapper.get_webdriver()
        self.driver.get("https://rozetka.com.ua")

    def teardown(self):
        self.driver.close()
