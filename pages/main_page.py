import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):

    TOP_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    
    @allure.step("Принять файлы cookie")
    def accept_cookies(self):
        self.click_element(self.COOKIE_ACCEPT_BUTTON)

    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_top_button_order(self):
        self.click_element(self.TOP_BUTTON_ORDER)

    @allure.step("Прокрутить страницу и кликнуть по нижней кнопке 'Заказать'")
    def click_bottom_button_order(self):
        self.scroll_to_element(self.BOTTOM_BUTTON_ORDER)
        self.click_element(self.BOTTOM_BUTTON_ORDER)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться загрузки страницы Дзена")
    def wait_for_dzen_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(Urls.DZEN_URL))