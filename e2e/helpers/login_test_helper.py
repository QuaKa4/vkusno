from e2e.pages.common import Passwords, Users
from e2e.pages.login_page import LoginPage


def login_test_helper(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_url()
    login_page.set_username(Users.USERNAME)
    login_page.set_password(Passwords.PASSWORD)
    login_page.submit_button_press()


