import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MainPage.BASE_URL)
        main_page = MainPage(cls.driver)
        main_page.accept_cookies()

    @pytest.mark.parametrize(
            "order_button, first_name, last_name, address, metro, phone, date, rental_period, color, comment",
            [
                (MainPage.TOP_BUTTON_ORDER, "Иван", "Иванов", "Ул. Пушкина, д. 10", 
                OrderPage.METRO_STATION_CHERKIZOVSKAYA, "88005553535", "30.06.2026", 
                OrderPage.RENTAL_PERIOD_ONE_DAY, OrderPage.BLACK_COLOR_CHECKBOX, "Позвоните за час"),
                
                (MainPage.BOTTOM_BUTTON_ORDER, "Петр", "Сидоров", "Ул. Ленина, д. 22", 
                OrderPage.METRO_STATION_SOKOLNIKI, "+79998887766", "11.06.2026", 
                OrderPage.RENTAL_PERIOD_TWO_DAYS, OrderPage.GREY_COLOR_CHECKBOX, " ")
            ]
    )

    def test_order_scooter_flow_success(self, order_button, first_name, last_name, address, metro, phone, date, rental_period, color, comment):
        self.driver.get(MainPage.BASE_URL)

        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        self.driver.find_element(*order_button).click()
        order_page.fill_client_info(first_name, last_name, address, metro, phone)
        order_page.fill_rent_info(date, rental_period, color, comment)
        assert "Заказ оформлен" in order_page.get_success_popup_text()

        self.driver.find_element(*OrderPage.CLOSE_POPUP_FORM).click()

        main_page.click_scooter_logo()
        assert self.driver.current_url == MainPage.BASE_URL

        main_page.click_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains("dzen.ru"))
        assert "dzen.ru" in self.driver.current_url
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        