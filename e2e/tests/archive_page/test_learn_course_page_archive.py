import time

from e2e.helpers.login_test_helper import login_test_helper
from e2e.pages.main_page import MainPage, LeftMenu


def test_learn_course_page_archive(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    time.sleep(4)
    main_page.wait_for_load()
    left_menu = LeftMenu(driver)
    left_menu.wait_for_load()
    learn_courses_page = left_menu.navigate_to_learn_courses()
    learn_courses_page.wait_for_load()
    learn_courses_page.add_to_archive()
    archive_page = left_menu.navigate_to_archive()
    archive_page.wait_for_load()
    learn_courses_page.remove_from_archive()
    left_menu.navigate_to_learn_courses()
    learn_courses_page.course_delete()
    driver.quit()
