import pytest
from pages.questions_about_important_page import QuestionsAboutImportant
from constants import QuestionsConstants
from urls import Urls


class TestPraktikum:

    @pytest.mark.parametrize(
            "question_locator, answer_locator, expected_question, expected_answer",
            [
                (QuestionsAboutImportant.FIRST_QUESTION, QuestionsAboutImportant.FIRST_ANSWER,
                QuestionsConstants.Q1, QuestionsConstants.A1),
            
                (QuestionsAboutImportant.SECOND_QUESTION, QuestionsAboutImportant.SECOND_ANSWER, 
                QuestionsConstants.Q2, QuestionsConstants.A2),
            
                (QuestionsAboutImportant.THIRD_QUESTION, QuestionsAboutImportant.THIRD_ANSWER, 
                QuestionsConstants.Q3, QuestionsConstants.A3),
            
                (QuestionsAboutImportant.FOURTH_QUESTION, QuestionsAboutImportant.FOURTH_ANSWER, 
                QuestionsConstants.Q4, QuestionsConstants.A4),
            
                (QuestionsAboutImportant.FIFTH_QUESTION, QuestionsAboutImportant.FIFTH_ANSWER, 
                QuestionsConstants.Q5, QuestionsConstants.A5),
            
                (QuestionsAboutImportant.SIXTH_QUESTION, QuestionsAboutImportant.SIXTH_ANSWER, 
                QuestionsConstants.Q6, QuestionsConstants.A6),
            
                (QuestionsAboutImportant.SEVENTH_QUESTION, QuestionsAboutImportant.SEVENTH_ANSWER, 
                QuestionsConstants.Q7, QuestionsConstants.A7),
            
                (QuestionsAboutImportant.EIGHTH_QUESTION, QuestionsAboutImportant.EIGHTH_ANSWER, 
                QuestionsConstants.Q8, QuestionsConstants.A8)
            ]
    )

    def test_questions_about_important_shows_correct_answer(self, driver, question_locator, answer_locator, expected_question, expected_answer):
        questions_page = QuestionsAboutImportant(driver)
        questions_page.open_url(Urls.BASE_URL)

        questions_page.accept_cookies()

        actual_question = questions_page.get_question_text(question_locator)
        assert actual_question == expected_question

        questions_page.click_question(question_locator)

        actual_answer = questions_page.get_answer_text(answer_locator)
        assert actual_answer == expected_answer
        