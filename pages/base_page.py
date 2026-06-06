import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждать появления {locator} на странице")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Выполнить клик по элементу с локатором: {locator}")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Заполнить поле {locator} значением: {text}")
    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Прокрутить страницу до элемента с локатором: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    @allure.step("Открыть страницу по адресу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL браузера")
    def get_current_url(self):
        return self.driver.current_url
