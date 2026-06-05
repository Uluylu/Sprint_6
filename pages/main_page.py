from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    TOP_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']")
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/?yredirect=true"
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()

    def click_top_button_order(self):
        self.driver.find_element(*self.TOP_BUTTON_ORDER).click()

    def click_bottom_button_order(self):
        element = self.driver.find_element(*self.BOTTOM_BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        element.click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
