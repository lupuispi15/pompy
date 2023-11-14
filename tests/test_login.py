import time

from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base


class TestLogin(Base):

    def test_2_login(self):
        driver = self.driver
        driver.get(home_page.base_url)
        time.sleep(1)
        HomePage(driver).send_text_user("standard_user")
        time.sleep(1)
        HomePage(driver).send_password("secret_sauce")
        time.sleep(1)
        HomePage(driver).get_button()
        driver.get(home_page.base_url)

    def test_3_login_fail(self):
        driver = self.driver
        driver.get(home_page.base_url)
        HomePage(driver).send_text_user("standard_user")
        HomePage(driver).send_password("secret_sauce")
        time.sleep(1)
        HomePage(driver).borrar().clear()
        time.sleep(1)
        HomePage(driver).send_text_user("standard_use")
        HomePage(driver).get_button()
        HomePage(driver).view_error()
        self.assertTrue(HomePage(driver).view_error())
        self.assertEquals(HomePage(driver).view_error2(),"Epic sadface: Username and password do not match any user in this service")




