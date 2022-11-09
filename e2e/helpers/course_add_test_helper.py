import time

from e2e.helpers.login_test_helper import login_test_helper
from e2e.pages.learn_courses_page import LearnCoursesPage
from e2e.pages.main_page import MainPage


def tab_on_main_page(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    time.sleep(7)
    main_page.wait_for_load()

    courses_page = main_page.click_on_courses_card()
    courses_page.wait_for_load()
    courses_page.click_on_passing_course_button()

    learn_courses_page = LearnCoursesPage(driver)
    learn_courses_page.navigate_to_url()
    learn_courses_page.wait_for_load()

