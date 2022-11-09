from selenium.webdriver.common.by import By

from e2e.helpers.waiter import Wait
from e2e.pages.base_page import BasePage


class CoursePageLocators:
    passing_course_button = (
        By.XPATH, '//div[@data-appearance="aside"]//button[text()="Поступить на курс"][1]')


class CoursePage(BasePage):
    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *CoursePageLocators.passing_course_button)

    def click_on_passing_course_button(self):
        self.driver.find_element(*CoursePageLocators.passing_course_button).click()
