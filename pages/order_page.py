from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:
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


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_client_info(self, first_name, last_name, address, metro, phone):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.METRO_INPUT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(metro)).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_rent_info(self, date, rental_period, color, comment):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.DATE_INPUT)).send_keys(date)
        self.driver.find_element(*self.RENTAL_LOGO).click()
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(rental_period)).click()
        self.driver.find_element(*color).click()
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.CONFIRM_YES_BUTTON)).click()

    def get_success_popup_text(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.SUCCESS_POPUP_FORM))
        return self.driver.find_element(*self.SUCCESS_POPUP_FORM).text
