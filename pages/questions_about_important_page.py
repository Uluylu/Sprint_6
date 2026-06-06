import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QuestionsAboutImportant(BasePage):

    FIRST_QUESTION = (By.ID, "accordion__heading-0")
    SECOND_QUESTION = (By.ID, "accordion__heading-1")
    THIRD_QUESTION = (By.ID, "accordion__heading-2")
    FOURTH_QUESTION = (By.ID, "accordion__heading-3")
    FIFTH_QUESTION = (By.ID, "accordion__heading-4")
    SIXTH_QUESTION = (By.ID, "accordion__heading-5")
    SEVENTH_QUESTION = (By.ID, "accordion__heading-6")
    EIGHTH_QUESTION = (By.ID, "accordion__heading-7")

    FIRST_ANSWER = (By.ID, "accordion__panel-0")
    SECOND_ANSWER = (By.ID, "accordion__panel-1")
    THIRD_ANSWER = (By.ID, "accordion__panel-2")
    FOURTH_ANSWER = (By.ID, "accordion__panel-3")
    FIFTH_ANSWER = (By.ID, "accordion__panel-4")
    SIXTH_ANSWER = (By.ID, "accordion__panel-5")
    SEVENTH_ANSWER = (By.ID, "accordion__panel-6")
    EIGHTH_ANSWER = (By.ID, "accordion__panel-7")

    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")

    @allure.step("Принять файлы cookie")
    def accept_cookies(self):
        self.click_element(self.COOKIE_ACCEPT_BUTTON)

    @allure.step("Получить видимый текст вопроса")
    def get_question_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Прокрутить до вопроса и кликнуть по нему")
    def click_question(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить текст открывшегося ответа")
    def get_answer_text(self, locator):
        return self.find_element(locator).text
