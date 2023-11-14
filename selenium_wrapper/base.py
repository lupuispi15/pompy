import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Base(unittest.TestCase):
    driver = webdriver.Firefox()
    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

