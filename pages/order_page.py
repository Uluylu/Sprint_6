import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    FIRST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    METRO_STATION_CHERKIZOVSKAYA = (By.XPATH, "//div[contains(@class, 'select-search')]//*[text()='Черкизовская']")
    METRO_STATION_SOKOLNIKI = (By.XPATH, "//div[contains(@class, 'select-search')]//*[text()='Сокольники']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]")
    RENTAL_LOGO = (By.XPATH, "//div[text()='Про аренду']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_POPUP_FORM = (By.XPATH, "//div[text()='Заказ оформлен']")
    CLOSE_POPUP_FORM = (By.XPATH, "//button[text()='Посмотреть статус']")

    @allure.step("Заполнить персональные данные клиента")
    def fill_client_info(self, first_name, last_name, address, metro, phone):
        self.fill_field(self.FIRST_NAME_INPUT, first_name)
        self.fill_field(self.LAST_NAME_INPUT, last_name)
        self.fill_field(self.ADDRESS_INPUT, address)

        self.click_element(self.METRO_INPUT)
        self.click_element(metro)

        self.fill_field(self.PHONE_NUMBER_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить информацию об аренде и подтвердить заказ")
    def fill_rent_info(self, date, rental_period, color, comment):
        self.fill_field(self.DATE_INPUT, date)
        
        self.click_element(self.RENTAL_LOGO)
        self.click_element(self.RENTAL_PERIOD)
        
        self.click_element(rental_period)
        self.click_element(color)

        self.fill_field(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_YES_BUTTON)

    @allure.step("Получить текст подтверждения из всплывающего окна")
    def get_success_popup_text(self):
        return self.find_element(self.SUCCESS_POPUP_FORM).text
