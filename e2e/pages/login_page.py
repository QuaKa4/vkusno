from selenium.webdriver.common.by import By

from e2e.helpers.waiter import Wait
from e2e.pages.base_page import BasePage


class LoginPageLocators:
    dialog = (By.XPATH, '//*[@role="dialog"]')
    login_input = (By.CSS_SELECTOR, 'input[name="login"]')
    password_input = (By.CSS_SELECTOR, 'input[name="password"]')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')


class LoginPage(BasePage):
    url = 'learn?auth=login'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *LoginPageLocators.dialog)
        Wait.for_visibility(self.driver, *LoginPageLocators.submit_button)

    def set_username(self, username):
        username_input = self.driver.find_element(*LoginPageLocators.login_input)
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.password_input)
        password_input.send_keys(password)

    def submit_button_press(self):
        submit_button = self.driver.find_element(*LoginPageLocators.submit_button)
        submit_button.click()
