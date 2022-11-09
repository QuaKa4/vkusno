from e2e.helpers.course_add_test_helper import tab_on_main_page
from e2e.pages.learn_courses_page import LearnCoursesPage


def test_course_add(driver):
    tab_on_main_page(driver)
    learn_courses_page = LearnCoursesPage(driver)
    learn_courses_page.course_delete()
    driver.quit()
