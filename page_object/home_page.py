from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.input_user = 'user-name'
        self.input_password = 'password'
        self.button = 'login-button'
        self.xpath_page_init = '//*[@id="header_container"]/div[2]/span'
        self.container_error = '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]'
        self.error = 'Epic sadface: Username and password do not match any user in this service'

    def get_page_login(self):
        return self.driver.find_element(By.XPATH, self.xpath_image_login)

    def get_button(self):
        return self.driver.find_element(By.ID, self.button).click()

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def view_page(self):
        return self.get_page_login().is_displayed()

    def error_login(self):
        return self.driver.find_element(By.XPATH, self.container_error)

    def view_error(self):
        return self.error_login().is_displayed()

    def view_error2(self):
        return self.error_login().text

    def borrar(self):
        campo_texto = self.driver.find_element(By.ID, self.input_user)
        return campo_texto

