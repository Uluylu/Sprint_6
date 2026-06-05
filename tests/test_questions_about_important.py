import pytest
from selenium import webdriver
from pages.questions_about_important_page import QuestionsAboutImportant


class TestPraktikum:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(QuestionsAboutImportant.URL)
        questions_page = QuestionsAboutImportant(cls.driver)
        questions_page.accept_cookies()

    @pytest.mark.parametrize(
            "question_locator, answer_locator, expected_question, expected_answer",
            [
                (QuestionsAboutImportant.FIRST_QUESTION, QuestionsAboutImportant.FIRST_ANSWER,
                 "Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                (QuestionsAboutImportant.SECOND_QUESTION, QuestionsAboutImportant.SECOND_ANSWER, 
                "Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                (QuestionsAboutImportant.THIRD_QUESTION, QuestionsAboutImportant.THIRD_ANSWER, 
                "Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                (QuestionsAboutImportant.FOURTH_QUESTION, QuestionsAboutImportant.FOURTH_ANSWER, 
                "Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                (QuestionsAboutImportant.FIFTH_QUESTION, QuestionsAboutImportant.FIFTH_ANSWER, 
                "Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                (QuestionsAboutImportant.SIXTH_QUESTION, QuestionsAboutImportant.SIXTH_ANSWER, 
                "Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                (QuestionsAboutImportant.SEVENTH_QUESTION, QuestionsAboutImportant.SEVENTH_ANSWER, 
                "Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                (QuestionsAboutImportant.EIGHTH_QUESTION, QuestionsAboutImportant.EIGHTH_ANSWER, 
                "Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
            ]
    )

    def test_questions_about_important_shows_correct_answer(self, question_locator, answer_locator, expected_question, expected_answer):
        self.driver.get(QuestionsAboutImportant.URL)
        questions_page = QuestionsAboutImportant(self.driver)

        actual_question = questions_page.get_question_text(question_locator)
        assert actual_question == expected_question

        questions_page.click_question(question_locator)

        actual_answer = questions_page.get_answer_text(answer_locator)
        assert actual_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        