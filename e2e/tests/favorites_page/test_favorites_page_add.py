from e2e.helpers.course_add_test_helper import tab_on_main_page
from e2e.pages.main_page import LeftMenu


def test_learn_course_page_archive(driver):
    tab_on_main_page(driver)
    left_menu = LeftMenu(driver)
    left_menu.navigate_to_learn_courses()
    left_menu.wait_for_load()
    learn_courses_page = left_menu.navigate_to_learn_courses()
    learn_courses_page.wait_for_load()
    learn_courses_page.add_to_favorites()
    archive_page = left_menu.navigate_to_archive()
    archive_page.wait_for_load()
    driver.quit()
