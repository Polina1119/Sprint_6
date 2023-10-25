from time import sleep

import pytest

from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import MainPage
from pages.base_page import BasePage
from tests import data


class TestListQuestions:
    @pytest.mark.parametrize('question, answer, text', [
        (Main.QUESTION_1, Main.ANSWER_1, data.text1),
        (Main.QUESTION_2, Main.ANSWER_2, data.text2),
        (Main.QUESTION_3, Main.ANSWER_3, data.text3),
        (Main.QUESTION_4, Main.ANSWER_4, data.text4),
        (Main.QUESTION_5, Main.ANSWER_5, data.text5),
        (Main.QUESTION_6, Main.ANSWER_6, data.text6),
        (Main.QUESTION_7, Main.ANSWER_7, data.text7),
        (Main.QUESTION_8, Main.ANSWER_8, data.text8)
    ])
    def test_questions(self, driver, question, answer, text):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.scroll()
        main_page.click_question(question)
        base_page.find_element(answer)

        assert base_page.find_element(answer).text == text

