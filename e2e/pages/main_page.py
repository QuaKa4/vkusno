from selenium.webdriver.common.by import By

from e2e.helpers.waiter import Wait
from e2e.pages.archive.archive_page import ArchivePage
from e2e.pages.base_page import BasePage
from e2e.pages.classes_page.classes_page import ClassesPage
from e2e.pages.course_page import CoursePage
from e2e.pages.favorites.favorites_page import FavoritesPage
from e2e.pages.going_to_pass.going_to_pass_page import GoingToPassPage
from e2e.pages.learn_courses_page import LearnCoursesPage
from e2e.pages.out_archive.out_archive_page import OutArchivePage


class MainPageLocators:
    header = (By.CLASS_NAME, 'catalog-course-cards__cards')
    footer = (By.CLASS_NAME, 'marco-layout__nav')
    body = (By.CLASS_NAME, 'marco-layout')
    courses_card = (By.XPATH, '//*[@class="catalog-rich-card__link-wrapper"][1]')


class MainPage(BasePage):
    url = 'learn'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *MainPageLocators.header)
        Wait.for_visibility(self.driver, *MainPageLocators.body)
        Wait.for_visibility(self.driver, *MainPageLocators.footer)

    def click_on_courses_card(self) -> CoursePage:
        self.driver.find_element(*MainPageLocators.courses_card).click()
        return CoursePage(self.driver)


class LeftMenuLocators:
    menu_body = (By.XPATH, '//*[@aria-labelledby="learn-nav-menu-label"]')
    courses = (By.XPATH, '//*[@class="nav-menu__menu-toggler')
    link_classes = (By.XPATH, '//*[href = "/learn/classes"]')
    link_notification = (By.XPATH, '//*[href = "/notifications?type=learn"]')
    link_main_page = (By.XPATH, '//*[href = "/learn"]')
    main_page_link = (By.XPATH, '//header[@id="main-header"]/nav/a')
    now_courses = (By.XPATH, '//a[@href="/learn/courses"]')


class LeftMenu(MainPage):

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *LeftMenuLocators.menu_body)
        Wait.for_visibility(self.driver, *LeftMenuLocators.now_courses)

    def _courses_opening(self, link: str):
        _link = f'//a[@href = "{link}"]'
        if not self.driver.find_element(By.XPATH, _link):
            self.driver.find_element(*LeftMenuLocators.courses).click()
            self.driver.find_element(By.XPATH, _link).click()
        else:
            self.driver.find_element(By.XPATH, _link).click()

    def navigate_to_learn(self):
        course = self.driver.find_element(By.XPATH, '//*[@class="nav-menu__menu-toggler"]')
        return course

    def navigate_to_my_studying(self) -> MainPage:
        self.driver.find_element().click()
        return MainPage(self.driver)

    def navigate_to_learn_courses(self) -> LearnCoursesPage:
        self._courses_opening("/learn/courses")
        return LearnCoursesPage(self.driver)

    def navigate_to_favorites(self) -> FavoritesPage:
        self._courses_opening('/learn/courses/favorites')
        return FavoritesPage(self.driver)

    def navigate_to_wishlist(self) -> GoingToPassPage:
        self._courses_opening('/learn/courses/wishlist')
        return GoingToPassPage(self.driver)

    def navigate_to_archive(self) -> ArchivePage:
        self._courses_opening('/learn/courses/archive')
        return ArchivePage(self.driver)

    def navigate_to_classes(self) -> ClassesPage:
        self.driver.find_element(*LeftMenuLocators.link_classes).click()
        return ClassesPage(self.driver)

    def navigate_to_notifications(self) -> OutArchivePage:
        self.driver.find_element(*LeftMenuLocators.link_notification).click()
        return OutArchivePage(self.driver)
