import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from constants import OrderConstants
from urls import Urls


class TestOrderScooter:

    @pytest.mark.parametrize(
            "order_button, first_name, last_name, address, metro, phone, date, rental_period, color, comment",
            [
            (MainPage.TOP_BUTTON_ORDER, 
             OrderConstants.FIRST_NAME_1, OrderConstants.LAST_NAME_1, OrderConstants.ADDRESS_1, 
             OrderPage.METRO_STATION_CHERKIZOVSKAYA, OrderConstants.PHONE_1, OrderConstants.DATE_1, 
             OrderPage.RENTAL_PERIOD_ONE_DAY, OrderPage.BLACK_COLOR_CHECKBOX, OrderConstants.COMMENT_1),
            
            (MainPage.BOTTOM_BUTTON_ORDER, 
             OrderConstants.FIRST_NAME_2, OrderConstants.LAST_NAME_2, OrderConstants.ADDRESS_2, 
             OrderPage.METRO_STATION_SOKOLNIKI, OrderConstants.PHONE_2, OrderConstants.DATE_2, 
             OrderPage.RENTAL_PERIOD_TWO_DAYS, OrderPage.GREY_COLOR_CHECKBOX, OrderConstants.COMMENT_2)
        ]
    )

    def test_order_scooter_flow_success(self, driver, order_button, first_name, last_name, address, metro, phone, date, rental_period, color, comment):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()

        order_page = OrderPage(driver)

        main_page.click_element(order_button)
        order_page.fill_client_info(first_name, last_name, address, metro, phone)
        order_page.fill_rent_info(date, rental_period, color, comment)
        assert "Заказ оформлен" in order_page.get_success_popup_text()

        order_page.click_element(OrderPage.CLOSE_POPUP_FORM)

        main_page.click_scooter_logo()
        assert main_page.get_current_url() == Urls.BASE_URL

        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("dzen.ru"))
        assert "dzen.ru" in main_page.get_current_url()
