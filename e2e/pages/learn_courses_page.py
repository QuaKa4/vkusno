import time

from selenium.webdriver.common.by import By

from e2e.helpers.waiter import Wait
from e2e.pages.base_page import BasePage


class LearnCoursesPageLocators:
    course = (By.XPATH, '//div[@class="item-tile-list"]/div[1]')
    course_span = (By.XPATH,
                   '//div[@class="teachlearn-courses learn-courses"]//*[@class="svg-icon menu-more_icon svg-icon_inline ember-view"]')
    course_span_delete = (By.XPATH, '//button[text()="Покинуть"]')
    course_span_delete_success = (By.XPATH, '//button[text()="Да, покинуть"]')
    add_to_archive = (By.XPATH, '//button[text()="Переместить в архив"]')
    add_to_favorites = (By.XPATH, '//button[text()="Добавить в избранные"]')
    remove_from_favorites = (By.XPATH, '//button[text()="Убрать из избранных"]')
    remove_from_archive = (By.XPATH, '//button[text()="Вернуть из архива"]')


class LearnCoursesPage(BasePage):
    url = 'learn/courses'

    def __init__(self, driver):
        self.driver = driver

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *LearnCoursesPageLocators.course)

    def course_delete(self):
        self.driver.find_element(*LearnCoursesPageLocators.course_span).click()
        self.driver.find_element(*LearnCoursesPageLocators.course_span_delete).click()
        self.driver.find_element(*LearnCoursesPageLocators.course_span_delete_success).click()

    def add_to_archive(self):
        self.driver.find_element(*LearnCoursesPageLocators.course_span).click()
        time.sleep(1)
        self.driver.find_element(*LearnCoursesPageLocators.add_to_archive).click()

    def remove_from_archive(self):
        self.driver.find_element(*LearnCoursesPageLocators.course_span).click()
        time.sleep(1)
        self.driver.find_element(*LearnCoursesPageLocators.remove_from_archive).click()

    def add_to_favorites(self):
        self.driver.find_element(*LearnCoursesPageLocators.course_span).click()
        time.sleep(1)
        self.driver.find_element(*LearnCoursesPageLocators.add_to_favorites).click()

    def remove_from_archive(self):
        self.driver.find_element(*LearnCoursesPageLocators.course_span).click()
        time.sleep(1)
        self.driver.find_element(*LearnCoursesPageLocators.remove_from_favorites).click()
