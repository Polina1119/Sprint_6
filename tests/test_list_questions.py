from time import sleep

import pytest

from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import BasePage, MainPage


class TestListQuestions:
    @pytest.mark.parametrize('question, answer, text', [
        (Main.QUESTION_1, Main.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (Main.QUESTION_2, Main.ANSWER_2, "Пока что у нас так: один заказ — один самокат. " \
               "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (Main.QUESTION_3, Main.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. "
                                         "Мы привозим самокат 8 мая в течение дня. " \
               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
               "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (Main.QUESTION_4, Main.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (Main.QUESTION_5, Main.ANSWER_5, "Пока что нет! Но если что-то срочное "
                                         "— всегда можно позвонить в поддержку по красивому номеру 1010."),
        (Main.QUESTION_6, Main.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. " \
               "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
               "Зарядка не понадобится."),
        (Main.QUESTION_7, Main.ANSWER_7, "Да, пока самокат не привезли. "
                                         "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (Main.QUESTION_8, Main.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_questions(self, driver, question, answer, text):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.scroll()
        sleep(1)
        main_page.click_question(question)
        #sleep(1)

        assert driver.find_element(*answer).text == text
