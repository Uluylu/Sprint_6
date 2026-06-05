from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class QuestionsAboutImportant:
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
    URL = "https://qa-scooter.praktikum-services.ru/"
    
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()

    def get_question_text(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def click_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        element.click()

    def get_answer_text(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
