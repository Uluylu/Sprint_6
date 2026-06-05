import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    TOP_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    
    @allure.step("Принять файлы cookie")
    def accept_cookies(self):
        self.click_element(self.COOKIE_ACCEPT_BUTTON)

    @allure.step("Кликнуть по верхней кнопке «Заказать»")
    def click_top_button_order(self):
        self.click_element(self.TOP_BUTTON_ORDER)

    @allure.step("Прокрутить страницу и кликнуть по нижней кнопке «Заказать»")
    def click_bottom_button_order(self):
        self.scroll_to_element(self.BOTTOM_BUTTON_ORDER)
        self.click_element(self.BOTTOM_BUTTON_ORDER)

    @allure.step("Кликнуть по логотипу «Самокат»")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу «Яндекс»")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
