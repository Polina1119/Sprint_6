import allure
from locators.main_page_locators import MainPageLocators as Main
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем на логотип Яндекс')
    def click_logo_yandex(self):
        return self.find_element(Main.LOGO_YANDEX).click()

    @allure.step('Переходим на страницу Яндекс.Дзен')
    def go_to_dzen(self):
        return self.switch_to()

    @allure.step('Нажимаем на логотип Яндекс.Самокат')
    def click_logo_scooter(self):
        return self.find_element(Main.LOGO_SCOOTER).click()

    @allure.step('Скролл до списка вопросов')
    def scroll(self):
        element = self.find_element(Main.FAQ)
        return self.execute_script(element)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question):
        return self.find_element(question).click()




