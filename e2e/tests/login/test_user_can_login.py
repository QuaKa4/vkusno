from e2e.helpers.login_test_helper import login_test_helper


def test_user_can_login_with_correct_data(driver):
    login_test_helper(driver)
    driver.quit()
