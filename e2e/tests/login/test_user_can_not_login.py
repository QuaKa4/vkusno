from dataclasses import dataclass

from e2e.pages.common import Passwords
from e2e.pages.common import Users
from e2e.pages.login_page import LoginPage


class TestLoginWithWrongData:
    @dataclass
    class _TestCaseData:
        username: Users
        password: Passwords

    @staticmethod
    def _test_method(driver, test_case_data: _TestCaseData):
        login_page = LoginPage(driver)
        login_page.navigate_to_url()
        login_page.wait_for_load()
        login_page.set_username(test_case_data.username)
        login_page.set_password(test_case_data.password)
        login_page.submit_button_press()
        login_page.wait_for_load()

        driver.quit()

    def test_user_cant_login_with_wrong_username(self, driver):
        test_case_data = self._TestCaseData(username=Users.WRONG_USERNAME, password=Passwords.PASSWORD)
        self._test_method(driver, test_case_data)

    def test_user_cant_login_with_wrong_password(self, driver):
        test_case_data = self._TestCaseData(username=Users.USERNAME, password=Passwords.WRONG_PASSWORD)
        self._test_method(driver, test_case_data)

    def test_user_cant_login_with_wrong_username_and_password(self, driver):
        test_case_data = self._TestCaseData(username=Users.WRONG_USERNAME, password=Passwords.WRONG_PASSWORD)
        self._test_method(driver, test_case_data)
