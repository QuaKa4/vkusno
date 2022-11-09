from selenium.webdriver.common.by import By

from e2e.pages.base_page import BasePage


class ArchivePageLocators:
    course_on_archive_page = (By.XPATH, '//article/div/div/div/div[1]/a')


class ArchivePage(BasePage):
    url = 'learn/courses/archive'

    def _elements_to_wait(self):
        self.driver.find_element(*ArchivePageLocators.course_on_archive_page)

